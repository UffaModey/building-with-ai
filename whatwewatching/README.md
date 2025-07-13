# 🎬 WhatWeWatching

A minimalist, mood-based movie and series recommendation app built by **Fafacodes**.

> “Because Netflix asking me to choose is a microaggression.”

---

## 🧩 Problem It Solves

Endless scrolling. Indecisiveness. Too many options.  
**WhatWeWatching** solves content fatigue by giving you curated, mood-driven film or series recommendations using global trends and your personal preferences.

---

## 🌟 Features

- 🎭 Filter by mood-driven genres
- 🎞️ Choose between movies or series (with season & episode limits)
- 🌍 Filter by global cinema industries (Hollywood, Nollywood, Bollywood, etc.)
- 📅 Filter by release year
- 🎥 Filter by streaming platform
- 👤 Add actor/actress preferences
- 🤖 AI-powered recommendations using OpenAI
- 📺 Top-rated fallback recommendation when no filters are selected

---

## 🛠 Tech Stack

- **Python 3.11+**
- **Streamlit** – UI framework
- **OpenAI API** – Content generation and recommendation engine
- **Custom styling** – Brand colors, fonts (Montserrat + TT Commons Pro)

---

## 🚀 Running Locally

### 🔧 Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/) *(optional but recommended)*
- OpenAI API key (you’ll need to add it to

### 🔽 How to Pull and Run the Project Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/whatwewatching.git
   cd whatwewatching
   ```
2. **Add your OpenAI API key**
Create a .env file in the root folder and paste:
OPENAI_API_KEY=your-api-key-here
3. **Install dependencies in a virtual environment and run the app in the environment**
```bash
pip install -r requirements.txt
streamlit run main.py
```
