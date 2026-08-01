def clean(items):
    cleaned_items = []

    for item in items:

        # Skip items with no title
        if not item["title"]:
            continue

        # Remove extra spaces
        item["title"] = item["title"].strip()


        cleaned_items.append(item)

    return cleaned_items