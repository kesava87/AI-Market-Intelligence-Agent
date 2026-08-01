import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:3b"


def ask_ollama(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()

        result = response.json()

        return result["response"]

    except requests.exceptions.RequestException as e:
        print("Error communicating with Ollama:", e)
        return None