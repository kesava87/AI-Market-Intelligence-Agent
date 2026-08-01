import feedparser
from models.data_model import create_item


def collect():
    """
    Collect the latest news from OpenAI RSS feed.
    Returns a list of dictionaries.
    """

    rss_url = "https://openai.com/news/rss.xml"

    feed = feedparser.parse(rss_url)

    news = []

    for article in feed.entries[:10]:
        news.append(
            create_item(
                title=article.title,
                link=article.link,
                source="OpenAI"
            )
        )

    return news