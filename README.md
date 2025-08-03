# 🗣️ Literary Sentiment Analysis

## 📖 Análise de Sentimentos em Textos Literários com Azure Language Studio

Este projeto utiliza o serviço **Text Analytics** da Microsoft Azure (dentro do **Language Studio**) para identificar e classificar o sentimento de trechos literários. O objetivo é explorar como a Inteligência Artificial pode interpretar o **tom emocional** de textos escritos — seja ele **positivo**, **negativo**, **neutro** ou **misto**.

---

## 📌 Objetivos

- Praticar o uso da **análise de sentimentos** com Azure Language Studio
- Automatizar a análise de múltiplos trechos com **Python**
- Compreender melhor a **emoção literária** expressa por autores
- Aplicar boas práticas de manipulação de APIs e segurança com `.env`

---

## 🔧 Tecnologias e Ferramentas

- [Azure Speech Studio](https://speech.microsoft.com/)
- [Azure Language Studio](https://language.azure.com/)
- Python 3.10+
- Bibliotecas Python:
  - `requests`
  - `dotenv`
  - `json`

---

## 📁 Estrutura do Projeto

>literary-sentiment-analysis<br>
>│<br>
>├── texts<br>
>│ ├── dom_casmurro.txt<br>
>│ └── o_alquimista.txt<br>
>│<br>
>├── scripts<br> 
>│ └── analyze_sentiment.py<br> 
>│<br>
>├── results<br> 
>│ ├── o_alquimista_analysis.json<br> 
>│ └── o_alquimista_analysis.json<br>
>|<br>
>├── .env<br> 
>├── .env.example<br> 
>├── .gitignore <br>
>├── main.py <br>
>└── README.md<br>

