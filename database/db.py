import sqlite3

DATABASE_NAME = "database/ai_market.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            source TEXT,
            link TEXT UNIQUE,
            published_date TEXT,
            stars INTEGER,
            language TEXT,
            ai_summary TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_items(items):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    inserted = 0
    skipped = 0

    for item in items:

        try:

            cursor.execute("""
                INSERT INTO ai_news (
                    title,
                    description,
                    source,
                    link,
                    published_date,
                    stars,
                    language
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                item["title"],
                item["description"],
                item["source"],
                item["link"],
                item["published_date"],
                item["stars"],
                item["language"]
            ))

            inserted += 1

        except sqlite3.IntegrityError:

            skipped += 1

    connection.commit()

    connection.close()

    return inserted, skipped


def get_unsummarized_items():

    connection = sqlite3.connect(DATABASE_NAME)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM ai_news
        WHERE ai_summary IS NULL
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows


def update_summary(news_id, summary):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE ai_news
        SET ai_summary = ?
        WHERE id = ?
    """, (summary, news_id))

    connection.commit()

    connection.close()
def get_all_summaries():

    connection = sqlite3.connect(DATABASE_NAME)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            title,
            ai_summary,
            source,
            published_date
        FROM ai_news
        WHERE ai_summary IS NOT NULL
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows   
def get_all_news():

    """
    Returns all stored AI news and GitHub repositories.
    """

    connection = sqlite3.connect(DATABASE_NAME)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM ai_news
        ORDER BY published_date DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows