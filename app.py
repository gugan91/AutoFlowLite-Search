import streamlit as st
import requests
import os
from ctransformers import AutoModelForCausalLM

st.set_page_config(page_title="AutoFlowLite Smart Assistant 🧠", layout="centered")

@st.cache_resource
def load_model():
    return AutoModelForCausalLM.from_pretrained(
        "TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
        model_file="mistral-7b-instruct-v0.1.Q4_K_M.gguf",
        model_type="mistral"
    )

model = load_model()

SERP_API_KEY = os.getenv("SERP_API_KEY", "your-serpapi-key")

def fetch_snippets(query):
    try:
        url = "https://serpapi.com/search"
        params = {"q": query, "api_key": SERP_API_KEY, "engine": "google"}
        response = requests.get(url, params=params)
        data = response.json()
        snippets = [res["snippet"] for res in data.get("organic_results", []) if "snippet" in res]
        return snippets[:3]
    except Exception as e:
        print("SerpAPI Error:", e)
        return []

def summarize_with_mistral(question, snippets):
    joined = "\n".join(snippets)
    prompt = f"""You are a helpful assistant. Based on these real-time search results, answer the question below clearly in 2–3 sentences.

Question: {question}

Search Results:
{joined}

Answer:"""
    return model(prompt, max_new_tokens=200)

def fallback_answer(question):
    prompt = f"""You are a helpful assistant. Answer the question below clearly in 2–3 sentences.

Question: {question}

Answer:"""
    return model(prompt, max_new_tokens=200)

st.title("🔍 AutoFlowLite – Free AI Answer Assistant")
st.markdown("Ask anything and get a clear, real-time AI summary. No links, no cost.")

question = st.text_input("🧠 Your question:", placeholder="e.g. What is quantum computing?")

if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Fetching answer..."):
            snippets = fetch_snippets(question)
            if snippets:
                answer = summarize_with_mistral(question, snippets)
                st.success("✅ Answer:")
                st.markdown(answer)
            else:
                fallback = fallback_answer(question)
                st.warning("No search results found. Here's an AI answer instead:")
                st.markdown(fallback)
