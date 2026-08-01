from datetime import datetime

from database.db import get_all_news


def build_report_data(trend_report):
    """
    Prepare all the data required for the HTML report.
    """

    all_items = get_all_news()

    news_items = []
    github_projects = []

    for item in all_items:

        source = item["source"].lower()

        if "github" in source:
            github_projects.append(item)
        else:
            news_items.append(item)

    # ---------------------------------------
    # Structured Trend Data
    # ---------------------------------------

    structured = trend_report["structured_report"]

    report_data = {

        "generated_date": datetime.now().strftime("%d %B %Y %I:%M %p"),

        "executive_summary": structured["executive_summary"],

        "trends": structured["top_trends"],

        "technologies": structured["technologies"],

        "companies": structured["companies"],

        "projects": structured["projects"],

        "market_outlook": structured["market_outlook"],

        "recommendations": structured["recommendations"],

        "news_items": news_items,

        "github_projects": github_projects,

        "total_news": len(news_items),

        "total_github_projects": len(github_projects),

        "total_items": len(all_items)

    }

    return report_data