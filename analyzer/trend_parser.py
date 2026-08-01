"""
=========================================================
Module Name : trend_parser.py
Purpose     : Parse AI-generated market reports into a
              structured Python dictionary.

Author      : AI Market Intelligence Platform
Version     : 4.0
=========================================================
"""

import re


# =========================================================
# REPORT HEADINGS
# =========================================================

SECTION_HEADINGS = {

    "executive_summary": [
        "EXECUTIVE SUMMARY"
    ],

    "top_trends": [
        "TOP 5 AI TRENDS",
        "TOP AI TRENDS",
        "KEY TRENDS",
        "AI TRENDS"
    ],

    "technologies": [
        "IMPORTANT TECHNOLOGIES",
        "KEY TECHNOLOGIES",
        "TECHNOLOGIES"
    ],

    "companies": [
        "COMPANIES MENTIONED",
        "COMPANIES",
        "ORGANIZATIONS"
    ],

    "projects": [
        "OPEN-SOURCE PROJECTS WORTH WATCHING",
        "OPEN SOURCE PROJECTS WORTH WATCHING",
        "OPEN-SOURCE PROJECTS",
        "OPEN SOURCE PROJECTS",
        "PROJECTS WORTH WATCHING",
        "PROJECTS"
    ],

    "market_outlook": [
        "MARKET OUTLOOK",
        "OUTLOOK"
    ],

    "recommendations": [
        "STRATEGIC RECOMMENDATIONS",
        "RECOMMENDATIONS",
        "SUGGESTIONS"
    ]
}


# =========================================================
# EMPTY STRUCTURE
# =========================================================

def create_structure():

    return {

        "executive_summary": "",

        "top_trends": [],

        "technologies": [],

        "companies": [],

        "projects": [],

        "market_outlook": "",

        "recommendations": []

    }


# =========================================================
# CLEAN MARKDOWN
# =========================================================

def clean_text(text):

    text = text.strip()

    # Remove markdown headings

    text = re.sub(r"^#{1,6}\s*", "", text)

    # Remove bullets

    text = re.sub(r"^[-*•>]+\s*", "", text)

    # Remove numbering

    text = re.sub(r"^\(?\d+\)?[.)\-:]*\s*", "", text)

    # Remove bold

    text = text.replace("**", "")

    text = text.replace("__", "")

    text = text.replace("`", "")

    # Collapse whitespace

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# =========================================================
# REMOVE DUPLICATES
# =========================================================

def unique(items):

    output = []

    seen = set()

    for item in items:

        key = item.lower().strip()

        if not key:

            continue

        if key in seen:

            continue

        seen.add(key)

        output.append(item.strip())

    return output


# =========================================================
# DETECT REPORT SECTION
# =========================================================

def detect_heading(line):
    """
    Detect ONLY actual markdown headings.

    This fixes the bug where normal sentences
    containing the word 'summary' or 'outlook'
    were incorrectly treated as section headers.
    """

    text = line.strip()

    if not text.startswith("#"):

        return None

    cleaned = clean_text(text).upper()

    for section, headings in SECTION_HEADINGS.items():

        for heading in headings:

            if cleaned == heading:

                return section

    return None


# =========================================================
# CLEAN FINAL LIST
# =========================================================

def finalize_list(items):

    cleaned = []

    for item in items:

        item = clean_text(item)

        if not item:

            continue

        cleaned.append(item)

    return unique(cleaned)


# =========================================================
# JOIN PARAGRAPH
# =========================================================

def finalize_paragraph(lines):

    if not lines:

        return ""

    paragraph = " ".join(lines)

    paragraph = re.sub(r"\s+", " ", paragraph)

    return paragraph.strip()
    # =========================================================
# MAIN PARSER
# =========================================================

def parse_trend_report(report_text):
    """
    Parse the AI-generated market report into
    a structured dictionary.
    """

    sections = create_structure()

    current_section = None

    executive_lines = []
    outlook_lines = []

    # ---------------------------------------------
    # Process report line by line
    # ---------------------------------------------

    for raw_line in report_text.splitlines():

        line = raw_line.strip()

        if not line:
            continue

        # ---------------------------------------------
        # Ignore separator lines
        # ---------------------------------------------

        if re.fullmatch(r"[-=_]{3,}", line):
            continue

        # ---------------------------------------------
        # Detect markdown heading
        # ---------------------------------------------

        heading = detect_heading(line)

        if heading is not None:

            current_section = heading

            continue

        # ---------------------------------------------
        # Clean current line
        # ---------------------------------------------

        cleaned = clean_text(line)

        if not cleaned:
            continue

        # ---------------------------------------------
        # Store according to current section
        # ---------------------------------------------

        if current_section == "executive_summary":

            executive_lines.append(cleaned)

        elif current_section == "top_trends":

            sections["top_trends"].append(cleaned)

        elif current_section == "technologies":

            sections["technologies"].append(cleaned)

        elif current_section == "companies":

            sections["companies"].append(cleaned)

        elif current_section == "projects":

            sections["projects"].append(cleaned)

        elif current_section == "market_outlook":

            outlook_lines.append(cleaned)

        elif current_section == "recommendations":

            sections["recommendations"].append(cleaned)

    # =====================================================
    # Build paragraphs
    # =====================================================

    sections["executive_summary"] = finalize_paragraph(
        executive_lines
    )

    sections["market_outlook"] = finalize_paragraph(
        outlook_lines
    )

    # =====================================================
    # Clean Lists
    # =====================================================

    sections["top_trends"] = finalize_list(
        sections["top_trends"]
    )

    sections["technologies"] = finalize_list(
        sections["technologies"]
    )

    sections["companies"] = finalize_list(
        sections["companies"]
    )

    sections["projects"] = finalize_list(
        sections["projects"]
    )

    sections["recommendations"] = finalize_list(
        sections["recommendations"]
    )

    # =====================================================
    # Remove invalid entries
    # =====================================================

    for key in [

        "top_trends",
        "technologies",
        "companies",
        "projects",
        "recommendations"

    ]:

        cleaned = []

        for item in sections[key]:

            if len(item.strip()) < 2:
                continue

            if item.lower() in {

                "not enough evidence.",
                "not enough evidence"

            }:
                continue

            cleaned.append(item)

        sections[key] = cleaned

    # =====================================================
    # Default values
    # =====================================================

    if not sections["executive_summary"]:

        sections["executive_summary"] = (
            "No executive summary was generated."
        )

    if not sections["market_outlook"]:

        sections["market_outlook"] = (
            "No market outlook was generated."
        )

    if not sections["recommendations"]:

        sections["recommendations"] = [

            "Continue monitoring AI market developments.",

            "Collect additional AI news sources.",

            "Review emerging technologies regularly."

        ]

    return sections