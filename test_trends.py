from database.db import get_all_summaries
from analyzer.trend_analyzer import analyze_trends


summaries = get_all_summaries()

report = analyze_trends(summaries)

print("\n========== AI MARKET REPORT ==========\n")

print(report)