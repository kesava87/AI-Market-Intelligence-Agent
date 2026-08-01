"""
=========================================================
Module Name : trend_analyzer.py
Purpose     : Generate AI market intelligence analysis
              using Ollama and convert it into
              structured business insights.

Author      : AI Market Intelligence Platform
Version     : 3.1
=========================================================
"""

from analyzer.ollama_client import ask_ollama
from analyzer.trend_parser import parse_trend_report


# =========================================================
# BUILD SUMMARY TEXT
# =========================================================

def prepare_summaries(summaries):
    """
    Convert database rows into a single clean text block.

    Parameters
    ----------
    summaries : list

    Returns
    -------
    str
    """

    collected = []

    for row in summaries:

        try:
            summary = row["ai_summary"]
        except (KeyError, IndexError):
            continue

        if summary is None:
            continue

        summary = str(summary).strip()

        if not summary:
            continue

        collected.append(summary)

    return "\n\n".join(collected)


# =========================================================
# BUILD PROMPT
# =========================================================

def build_prompt(summary_text):
    """
    Build the production prompt used by Ollama.
    """

    return f"""
You are a Senior AI Market Intelligence Analyst.

Your responsibility is to produce a professional market
intelligence report ONLY from the supplied summaries.

=========================================================
IMPORTANT RULES
=========================================================

1. ONLY use the supplied summaries.

2. DO NOT use your own knowledge.

3. DO NOT invent:

- Companies
- Technologies
- Products
- Frameworks
- Statistics
- Market predictions

4. If the summaries do not provide enough evidence,
write:

Not enough evidence.

5. Never mention technologies that are not present in
the summaries.

6. Never add companies that are not mentioned.

7. Keep the language professional and objective.

8. Do not repeat the same information across sections.

=========================================================
OUTPUT FORMAT
=========================================================

Use EXACTLY these headings.

### Executive Summary

Write one concise executive summary.

---------------------------------------------------------

### Top 5 AI Trends

1.
2.
3.
4.
5.

---------------------------------------------------------

### Important Technologies

1.
2.
3.
4.
5.

---------------------------------------------------------

### Companies Mentioned

1.
2.
3.
4.
5.

---------------------------------------------------------

### Open-source Projects Worth Watching

1.
2.
3.
4.
5.

---------------------------------------------------------

### Market Outlook

Write one business outlook paragraph.

---------------------------------------------------------

### Strategic Recommendations

1.
2.
3.
4.
5.

=========================================================
SUMMARIES
=========================================================

{summary_text}
"""


# =========================================================
# TREND ANALYSIS
# =========================================================

def analyze_trends(summaries):
    """
    Generate market intelligence from AI summaries.

    Parameters
    ----------
    summaries : list
        Database rows containing AI-generated summaries.

    Returns
    -------
    dict
        {
            raw_report,
            structured_report,
            generated_from
        }
    """

    # ---------------------------------------------
    # Prepare Summary Text
    # ---------------------------------------------

    summary_text = prepare_summaries(summaries)

    if not summary_text:

        empty_report = {
            "raw_report": "No AI summaries available for analysis.",
            "structured_report": {
                "executive_summary":
                    "No AI summaries were available for trend analysis.",

                "top_trends": [],

                "technologies": [],

                "companies": [],

                "projects": [],

                "market_outlook":
                    "Not enough evidence.",

                "recommendations": [
                    "Collect additional AI news before generating a report."
                ]
            },
            "generated_from": 0
        }

        return empty_report

    # ---------------------------------------------
    # Build Prompt
    # ---------------------------------------------

    prompt = build_prompt(summary_text)

    # ---------------------------------------------
    # Generate Report Using Ollama
    # ---------------------------------------------

    raw_report = ask_ollama(prompt)

    # ---------------------------------------------
    # Validate Response
    # ---------------------------------------------

    if raw_report is None:
        raw_report = ""

    raw_report = raw_report.strip()

    if not raw_report:

        raw_report = """
### Executive Summary

No report generated.

### Top 5 AI Trends

Not enough evidence.

### Important Technologies

Not enough evidence.

### Companies Mentioned

Not enough evidence.

### Open-source Projects Worth Watching

Not enough evidence.

### Market Outlook

Not enough evidence.

### Strategic Recommendations

Collect additional AI news.
"""

    # ---------------------------------------------
    # Parse Structured Report
    # ---------------------------------------------

    structured_report = parse_trend_report(raw_report)

    # ---------------------------------------------
    # Final Result
    # ---------------------------------------------

    return {
        "raw_report": raw_report,
        "structured_report": structured_report,
        "generated_from": len(summaries),
    }