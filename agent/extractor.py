import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

HF_MODEL = os.environ.get("HF_MODEL", "mistralai/Mistral-Nemo-Instruct-2407")
HF_TOKEN = os.environ.get("HF_API_TOKEN")

if not HF_TOKEN:
    raise RuntimeError("Set HF_API_TOKEN in the .env file")

BASE_URL = f"https://router.huggingface.co/hf-inference/{HF_MODEL}"
CHAT_URL = f"https://router.huggingface.co/hf-inference/{HF_MODEL}/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


def extract_structured(prompt, max_new_tokens=256):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": max_new_tokens}
    }

    r = requests.post(BASE_URL, headers=HEADERS, json=payload, timeout=60)
    r.raise_for_status()
    resp = r.json()

    # HF responses can be list or dict
    if isinstance(resp, list):
        text = resp[0].get("generated_text", "")
    else:
        text = resp.get("generated_text", "")

    # Attempt to extract JSON even if text has extra words
    # Example: "Here is the JSON:\n{"key": "value"}"
    try:
        obj_start = text.find("{")
        obj_end = text.rfind("}")
        if obj_start != -1 and obj_end != -1:
            json_str = text[obj_start:obj_end + 1]
            return json.loads(json_str)
    except Exception:
        pass

    return {"raw_text": text}


def chat_extract(messages, max_tokens=512):
    """messages = [{"role": "user"|"assistant"|"system", "content": "..." }]"""

    payload = {
        "messages": messages,
        "max_tokens": max_tokens
    }

    r = requests.post(CHAT_URL, headers=HEADERS, json=payload, timeout=60)
    r.raise_for_status()
    resp = r.json()

    # Handle HF v1-style format
    if "choices" in resp and len(resp["choices"]) > 0:
        choice = resp["choices"][0]

        if "message" in choice:
            return choice["message"]["content"]

        if "text" in choice:
            return choice["text"]

    # Fallback
    return resp
