from analyzer.summarizer import summarize_item

item = {
    "title": "TensorFlow",
    "description": "An end-to-end open-source machine learning platform developed by Google.",
    "source": "GitHub"
}

summary = summarize_item(item)

print("\n========== SUMMARY ==========\n")
print(summary)