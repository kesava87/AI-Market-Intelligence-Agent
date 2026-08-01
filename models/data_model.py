def create_item(
    title,
    source,
    description=None,
    link=None,
    published_date=None,
    stars=None,
    language=None,
    metadata=None
):
    if metadata is None:
        metadata = {}

    return {
        "title": title,
        "description": description,
        "link": link,
        "source": source,
        "published_date": published_date,
        "stars": stars,
        "language": language,
        "metadata": metadata
    }