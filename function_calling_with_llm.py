import os
from dotenv import load_dotenv
from google import genai
import json
import re

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def calculate_sum(a, b):
    return {"result": a + b, "expression": f"{a} + {b} = {a + b}"}

def get_weather(location):
    return {"location": location, "temp": "22°C", "condition": "Güneşli"}

TOOLS_SCHEMA = [
    {
        "name": "calculate_sum",
        "description": "İki sayıyı toplar",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "integer"},
                "b": {"type": "integer"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "get_weather",
        "description": "Verilen konumdaki anlık hava durumunu getirir",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            },
            "required": ["location"]
        }
    }
]

AVAILABLE_FUNCTIONS = {
    "calculate_sum": calculate_sum,
    "get_weather": get_weather
}


def router_llm(user_query: str) -> dict:
    prompt = f"""
Sen bir yönlendirici asistansın. Kullanıcının sorusuna göre hangi aracı kullanman gerektiğine karar ver.

Kullanılabilir araçlar:
{json.dumps(TOOLS_SCHEMA, ensure_ascii=False, indent=2)}

SADECE şu formatta JSON döndür, başka hiçbir şey yazma:
{{"name": "fonksiyon_adı", "parameters": {{...}}}}

Eğer hiçbir araç uygun değilse:
{{"name": null, "parameters": {{}}}}

Kullanıcının sorusu: {user_query}
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    cleaned = re.sub(r"```json|```", "", response.text).strip()
    tool_call = json.loads(cleaned)

    print(f"[Router LLM] Karar: {tool_call}")
    return tool_call


def run_tool(tool_call: dict) -> any:
    func_name = tool_call.get("name")

    if not func_name or func_name not in AVAILABLE_FUNCTIONS:
        print("[Tool Runner] Uygun araç bulunamadı.")
        return None

    func = AVAILABLE_FUNCTIONS[func_name]
    result = func(**tool_call["parameters"])

    print(f"[Tool Runner] '{func_name}' çalıştı → {result}")
    return result


def responder_llm(user_query: str, tool_name: str, tool_result: any) -> str:
    prompt = f"""
Sen yardımsever bir asistansın. Kullanıcının sorusunu, elindeki araç sonucunu kullanarak doğal bir dille cevapla.

Kullanıcının sorusu: {user_query}
Kullanılan araç: {tool_name}
Araç sonucu: {json.dumps(tool_result, ensure_ascii=False)}

Kısa, net ve samimi bir cevap ver.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text.strip()


def agent(user_query: str):
    print(f"\n{'='*50}")
    print(f"Kullanıcı: {user_query}")
    print('='*50)

    tool_call = router_llm(user_query)

    tool_result = run_tool(tool_call)


    if tool_result is None:
        print("[Responder LLM] Tool yok, direkt cevap veriliyor...")
        direct_prompt = f"Kullanıcının sorusunu cevapla: {user_query}"
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=direct_prompt
        )
        print(f"\nSonuç: {response.text.strip()}")
        return

    final_answer = responder_llm(user_query, tool_call["name"], tool_result)

    print(f"\nSonuç: {final_answer}")


# agent("10 + 20 kaç eder?")
# agent("İstanbul'da hava nasıl?")
agent("benimle sohbet et")
