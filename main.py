from collectors.manager import collect_all
from processors.cleaner import clean

from database.db import (
    create_database,
    save_items,
    get_unsummarized_items,
    update_summary,
    get_all_summaries,
)

from analyzer.summarizer import summarize_item
from analyzer.trend_analyzer import analyze_trends

from reports.report_generator import generate_report

from email_sender import send_email


def main():
    """
    Main entry point for the AI Market Intelligence Platform.
    """

    print("\n========== AI Market Intelligence Agent ==========\n")

    # --------------------------------------------------
    # Create Database
    # --------------------------------------------------

    create_database()

    # --------------------------------------------------
    # Collect Data
    # --------------------------------------------------

    all_data = collect_all()

    print(f"Collected: {len(all_data)}")

    # --------------------------------------------------
    # Clean Data
    # --------------------------------------------------

    clean_data = clean(all_data)

    print(f"Cleaned: {len(clean_data)}")

    # --------------------------------------------------
    # Save Data
    # --------------------------------------------------

    inserted, skipped = save_items(clean_data)

    # --------------------------------------------------
    # Generate AI Summaries
    # --------------------------------------------------

    items = get_unsummarized_items()

    print(f"\nGenerating AI summaries for {len(items)} items...\n")

    summarized = 0

    for item in items:

        summary = summarize_item(item)

        if summary:
            update_summary(item["id"], summary)
            summarized += 1

            print(f"✓ {item['title']}")

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    print("\n========== SUMMARY ==========")
    print(f"Collected Items     : {len(all_data)}")
    print(f"Cleaned Items       : {len(clean_data)}")
    print(f"Inserted Items      : {inserted}")
    print(f"Skipped Duplicates  : {skipped}")
    print(f"AI Summaries        : {summarized}")
    print("=============================")

    # --------------------------------------------------
    # Generate Trend Analysis
    # --------------------------------------------------

    print("\nGenerating AI Market Trend Analysis...\n")

    summaries = get_all_summaries()

    print(f"Total summaries fetched: {len(summaries)}")

    if summaries:

        print("\n========== SAMPLE SUMMARY ==========\n")

        print("TITLE:")
        print(summaries[0]["title"])

        print("\nAI SUMMARY:")
        print(summaries[0]["ai_summary"])

        print("\n====================================\n")

        trend_report = analyze_trends(summaries)

        print("\n========== PARSED EXECUTIVE SUMMARY ==========\n")
        print(trend_report["structured_report"]["executive_summary"])
        print("\n==============================================\n")

        print("\n========== RAW TREND REPORT ==========\n")
        print(trend_report["raw_report"])
        print("\n======================================\n")

        print("✓ Trend analysis completed")

    else:

        print("No summaries available.")
        return

    # --------------------------------------------------
    # Generate HTML Report
    # --------------------------------------------------

    print("\nGenerating HTML Report...\n")

    report_path = generate_report(trend_report)

    print("\n=====================================")
    print("HTML Report Generated Successfully")
    print(report_path)
    print("=====================================")

    print("\n✓ HTML report generated successfully")
    print(f"Report Location: {report_path}")

    # --------------------------------------------------
    # Send Email
    # --------------------------------------------------

    print("\nSending email report...")
    send_email()

    # --------------------------------------------------
    # Completed
    # --------------------------------------------------

    print("\n========== PROCESS COMPLETED ==========")
    print("AI Market Intelligence Report is ready.")
    print("=======================================\n")


if __name__ == "__main__":
    main()