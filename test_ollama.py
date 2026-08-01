from analyzer.ollama_client import ask_ollama

prompt = """
Explain what Artificial Intelligence is in 50 words.
"""

response = ask_ollama(prompt)

print("\n========== AI RESPONSE ==========\n")
print(response)