# AutoFlowLite Search 
A lightweight, real-time AI-powered search assistant that fetches the latest information from Google and summarizes it using a local large language model — 100% free and open-source.

---

## Live Demo
Try the app here:  
[Hugging Face Space](https://huggingface.co/spaces/gugandroid/autoflowlite-search)

---

## Features

- Real-time search with SerpAPI
- Summarized answers using local Mistral 7B LLM
- Free to use – no OpenAI or token-based billing
- Deployable on Hugging Face, Streamlit Cloud, or locally
- Fallback to LLM when no search data is found
- Clean interface — no raw search results shown

---

## Tech Stack

| Component  | Tool                            |
|------------|----------------------------------|
| Backend    | Python, Streamlit               |
| AI Model   | Mistral-7B via ctransformers     |
| Search API | SerpAPI (free tier)             |
| Hosting    | Hugging Face Spaces or local    |

---

## Installation

```bash
git clone https://github.com/your-username/AutoFlowLite-Search.git
cd AutoFlowLite-Search
pip install -r requirements.txt
streamlit run app.py
