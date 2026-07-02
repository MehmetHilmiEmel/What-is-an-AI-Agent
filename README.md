# LLM ile Function Calling & Google GenAI Agent Projesi

Bu depo (repository), Büyük Dil Modellerinin (LLM) dış dünyayla nasıl etkileşime girdiğini ve kendi araçlarını (tools) nasıl çalıştırdığını anlamak, ayrıca Google ADK frameworkünü kullanarak pratik bir yapay zeka ajanı (agent) geliştirmek için oluşturulmuş kapsamlı bir rehberdir.

Projenin sıfırdan yapım aşamalarını ve detaylı anlatımını içeren YouTube videosuna aşağıdaki bağlantıdan ulaşabilirsiniz:

📺 [YouTube Eğitim Videosunu İzle (https://youtu.be/X5eep2ywXVk)](#)

## 📌 İçindekiler

- [Proje Yapısı](#-proje-yapısı)
- [Kurulum ve Hazırlık](#️-kurulum-ve-hazırlık)
- [1. LLM Function Calling Sıfırdan Anlatım](#1-llm-function-calling-sıfırdan-anlatım)
- [2. Google ADK ile Ajan (Agent) Uygulaması](#2-google-genai-sdk-ile-ajan-agent-uygulaması)

## 📂 Proje Yapısı

```
├── .gitignore
├── .env                         # Çevre değişkenleri (API anahtarları vb.)
├── function_calling_with_llm.py # Sıfırdan Function Calling mantığı
└── my_agent_youtube_video/      # Google GenAI SDK Ajan projesi klasörü
```

## ⚙️ Kurulum ve Hazırlık

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla uygulayın:

**1. Depoyu bilgisayarınıza klonlayın:**

```bash
git clone https://github.com/MehmetHilmiEmel/What-is-an-AI-Agent.git
cd What-is-an-AI-Agent
```

**2. Sanal ortam (Virtual Environment) oluşturun ve aktif edin (Önerilir):**

```bash
# Windows için
python -m venv venv
venv\Scripts\activate

# macOS/Linux için
python3 -m venv venv
source venv/bin/activate
```

**3. Gerekli kütüphaneleri yükleyin:** (Gerekli paketleri `requirements.txt` dosyasına eklediyseniz)

```bash
pip install google-adk
```

## 1. LLM Function Calling Sıfırdan Anlatım

`function_calling_with_llm.py` dosyası, harici bir kütüphane bağımlılığı olmadan (veya temel düzeyde), bir dil modelinin kendisine verilen fonksiyon tanımlarını analiz ederek uygun parametrelerle nasıl "fonksiyon çağırma kararı" aldığını sıfırdan gösterir. LLM'lerin araç kullanma mantığını kavramak için harika bir başlangıç noktasıdır.

**Çalıştırma:**

Bu kodu çalıştırmak için terminalden projenin ana dizinindeyken aşağıdaki komutu yazmanız yeterlidir:

```bash
python function_calling_with_llm.py
```

## 2. Google GenAI SDK ile Ajan (Agent) Uygulaması

`my_agent_youtube_video` klasörünün içinde, Google'ın Google-ADK frameworkünü kullanan pratik ve akıllı bir arayüze sahip yapay zeka ajanı yer almaktadır.

**API Yapılandırması:**

Ajanın çalışabilmesi için Google API anahtarınızı tanımlamanız gerekmektedir. Projenin ana dizininde bir `.env` dosyası oluşturun (veya varsa düzenleyin) ve aşağıdaki değişkenleri ekleyin:

```
GOOGLE_GENAI_USE_ENTERPRISE=0
GOOGLE_API_KEY=AQ.Ab...........sizin_api_anahtariniz_buraya...........
```

⚠️ **Önemli:** API anahtarınız size özeldir. Güvenliğiniz için `.env` dosyanızı asla GitHub gibi ortamlarda paylaşmayın (`.gitignore` dosyasının bu dosyayı kapsadığından emin olun).

**Çalıştırma:**

Klasörün içerisine girmekle uğraşmadan, projenin ana dizinindeyken doğrudan aşağıdaki komut vasıtasıyla ajanı web arayüzü ile başlatabilirsiniz:

```bash
adk web
```

## 🎥 Eğitim Videosu

Bu projenin sıfırdan kodlanma aşamalarını, mantıksal arka planını ve adım adım canlı testlerini izlemek için hazırladığım YouTube videosuna göz atabilirsiniz:

👉 [AI Agent Nedir](https://youtu.be/X5eep2ywXVk)
