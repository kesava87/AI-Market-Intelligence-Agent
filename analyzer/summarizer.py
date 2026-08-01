from analyzer.ollama_client import ask_ollama


def summarize_item(item):

    prompt = f"""
You are an expert AI Market Analyst.

Your task is to summarize the following AI-related content.

Title:
{item["title"]}

Description:
{item["description"]}

Source:
{item["source"]}

Instructions:
- Write a clear summary.
- Keep it between 3 and 5 sentences.
- Highlight why it matters.
- Use professional language.
"""

    summary = ask_ollama(prompt)

    return summary