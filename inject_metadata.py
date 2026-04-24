"""
inject_metadata.py — adds canonical tags and JSON-LD schema to all 21 pages.
Run once then delete (or keep for future use when adding new pages).
"""

import re
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DATE_MODIFIED = "2026-04-24"

PUBLISHER = {"@type": "Organization", "name": "SoftwareSorted", "url": "https://softwaresorted.co.uk"}
AUTHOR    = {"@type": "Organization", "name": "SoftwareSorted"}

PAGES = [
    # ── HOMEPAGE ────────────────────────────────────────────────────────────
    {
        "file": "src/index.html",
        "canonical": "https://softwaresorted.co.uk/",
        "type": "WebSite",
        "title": "SoftwareSorted — Independent Software Reviews for UK Tradespeople",
        "description": "Independent software reviews for UK tradespeople. Original research, real user complaints, honest verdicts. No sponsored content.",
        "date_published": "2026-04-01",
    },
    # ── ELECTRICIANS ─────────────────────────────────────────────────────────
    {
        "file": "src/electricians/best-job-management-software.html",
        "canonical": "https://softwaresorted.co.uk/electricians/best-job-management-software/",
        "type": "Article",
        "title": "Best Job Management Software for UK Electricians (2026) — SoftwareSorted",
        "description": "The best job management software for UK electricians — independent reviews of Tradify, Powered Now, ServiceM8 and Jobber. Real pricing, honest catches, free trial links.",
        "date_published": "2026-04-01",
    },
    {
        "file": "src/electricians/tradify-review.html",
        "canonical": "https://softwaresorted.co.uk/electricians/tradify-review/",
        "type": "Review",
        "item_reviewed": "Tradify",
        "title": "Tradify Review 2026: Is It Worth It for UK Electricians? — SoftwareSorted",
        "description": "Honest Tradify review for UK electricians. Real pricing, the email footer problem, photo report gap, offline limitations, and a real job workflow walkthrough.",
        "date_published": "2026-04-01",
    },
    {
        "file": "src/electricians/powered-now-review.html",
        "canonical": "https://softwaresorted.co.uk/electricians/powered-now-review/",
        "type": "Review",
        "item_reviewed": "Powered Now",
        "title": "Powered Now Review 2026: Best for UK Electricians? — SoftwareSorted",
        "description": "Honest Powered Now review for UK electricians. CIS compliance, EICR certificates, offline mode, real pricing, and the field-staff pricing issue explained.",
        "date_published": "2026-04-01",
    },
    {
        "file": "src/electricians/servicem8-review.html",
        "canonical": "https://softwaresorted.co.uk/electricians/servicem8-review/",
        "type": "Review",
        "item_reviewed": "ServiceM8",
        "title": "ServiceM8 Review 2026: Is It Worth It for UK Electricians? — SoftwareSorted",
        "description": "Honest ServiceM8 review for UK electricians. Per-job pricing explained, Android limitations, client automation, CIS compliance gaps, and who it actually suits.",
        "date_published": "2026-04-01",
    },
    {
        "file": "src/electricians/jobber-review.html",
        "canonical": "https://softwaresorted.co.uk/electricians/jobber-review/",
        "type": "Review",
        "item_reviewed": "Jobber",
        "title": "Jobber Review 2026: Is It Worth It for UK Electricians? — SoftwareSorted",
        "description": "Honest Jobber review for UK electricians. Real pricing, QuickBooks sync issues, hidden per-user costs, offline mode update, and how it compares to Tradify.",
        "date_published": "2026-04-01",
    },
    {
        "file": "src/electricians/tradify-vs-servicem8.html",
        "canonical": "https://softwaresorted.co.uk/electricians/tradify-vs-servicem8/",
        "type": "Article",
        "title": "Tradify vs ServiceM8: Which Is Better for UK Electricians? (2026) — SoftwareSorted",
        "description": "Tradify vs ServiceM8 for UK electricians: Android support, pricing, CIS compliance compared. ServiceM8 is iOS-only — the decision is simpler than it looks.",
        "date_published": "2026-04-01",
    },
    {
        "file": "src/electricians/tradify-vs-powered-now.html",
        "canonical": "https://softwaresorted.co.uk/electricians/tradify-vs-powered-now/",
        "type": "Article",
        "title": "Tradify vs Powered Now: Which Is Better for UK Electricians? (2026) — SoftwareSorted",
        "description": "Tradify vs Powered Now compared for UK electricians. Certificates, CIS compliance, offline working, Xero integration, and real pricing — which wins for your business?",
        "date_published": "2026-04-01",
    },
    {
        "file": "src/electricians/tradify-vs-jobber.html",
        "canonical": "https://softwaresorted.co.uk/electricians/tradify-vs-jobber/",
        "type": "Article",
        "title": "Tradify vs Jobber: Which Is Better for UK Electricians? (2026) — SoftwareSorted",
        "description": "Tradify vs Jobber compared for UK electricians. Pricing, Xero vs QuickBooks integration, UK compliance, team size economics, and which is right for your business.",
        "date_published": "2026-04-01",
    },
    {
        "file": "src/electricians/servicem8-vs-powered-now.html",
        "canonical": "https://softwaresorted.co.uk/electricians/servicem8-vs-powered-now/",
        "type": "Article",
        "title": "ServiceM8 vs Powered Now: Which Is Better for UK Electricians? (2026) — SoftwareSorted",
        "description": "ServiceM8 vs Powered Now compared for UK electricians. Certificates, CIS compliance, Android support, automation, and pricing — which is right for your business?",
        "date_published": "2026-04-01",
    },
    {
        "file": "src/electricians/job-management-software-cis-vat.html",
        "canonical": "https://softwaresorted.co.uk/electricians/job-management-software-cis-vat/",
        "type": "Article",
        "title": "Job Management Software for CIS & VAT: Which UK Trade Apps Handle It? (2026) — SoftwareSorted",
        "description": "Which job management software correctly handles CIS reverse charge and Making Tax Digital for UK electricians? Honest comparison of Powered Now, Tradify, and ServiceM8 on compliance.",
        "date_published": "2026-04-01",
    },
    # ── PLUMBERS ──────────────────────────────────────────────────────────────
    {
        "file": "src/plumbers/best-job-management-software.html",
        "canonical": "https://softwaresorted.co.uk/plumbers/best-job-management-software/",
        "type": "Article",
        "title": "Best Job Management Software for UK Plumbers (2026) — SoftwareSorted",
        "description": "The best job management software for UK plumbers — independent reviews of Tradify, Powered Now, ServiceM8 and Jobber. Gas Safe compliance, Water Regulations Act, real pricing, honest catches.",
        "date_published": "2026-04-22",
    },
    {
        "file": "src/plumbers/tradify-review.html",
        "canonical": "https://softwaresorted.co.uk/plumbers/tradify-review/",
        "type": "Review",
        "item_reviewed": "Tradify",
        "title": "Tradify Review 2026: Is It Worth It for UK Plumbers? — SoftwareSorted",
        "description": "Honest Tradify review for UK plumbers. Real pricing, the email footer problem, no Gas Safe certificates, offline limitations, and a real boiler service workflow walkthrough.",
        "date_published": "2026-04-22",
    },
    {
        "file": "src/plumbers/powered-now-review.html",
        "canonical": "https://softwaresorted.co.uk/plumbers/powered-now-review/",
        "type": "Review",
        "item_reviewed": "Powered Now",
        "title": "Powered Now Review 2026: Is It Worth It for UK Plumbers? — SoftwareSorted",
        "description": "Honest Powered Now review for UK plumbers. Gas Safe certificates, CP12 landlord records, Legionella risk assessments, offline mode, CIS compliance, and real pricing.",
        "date_published": "2026-04-22",
    },
    {
        "file": "src/plumbers/servicem8-review.html",
        "canonical": "https://softwaresorted.co.uk/plumbers/servicem8-review/",
        "type": "Review",
        "item_reviewed": "ServiceM8",
        "title": "ServiceM8 Review 2026: Is It Worth It for UK Plumbers? — SoftwareSorted",
        "description": "Honest ServiceM8 review for UK plumbers. The Android limitation, per-job pricing, no Gas Safe certificates, and where it genuinely beats the competition.",
        "date_published": "2026-04-22",
    },
    {
        "file": "src/plumbers/jobber-review.html",
        "canonical": "https://softwaresorted.co.uk/plumbers/jobber-review/",
        "type": "Review",
        "item_reviewed": "Jobber",
        "title": "Jobber Review 2026: Is It Worth It for UK Plumbers? — SoftwareSorted",
        "description": "Honest Jobber review for UK plumbers. The pricing jump, QuickBooks sync issues, no Gas Safe certificates, client portal value, and when it makes sense for larger plumbing teams.",
        "date_published": "2026-04-22",
    },
    {
        "file": "src/plumbers/tradify-vs-servicem8.html",
        "canonical": "https://softwaresorted.co.uk/plumbers/tradify-vs-servicem8/",
        "type": "Article",
        "title": "Tradify vs ServiceM8: Which Is Better for UK Plumbers? (2026) — SoftwareSorted",
        "description": "Tradify vs ServiceM8 for UK plumbers: Android support, pricing, Gas Safe compliance compared. ServiceM8 is iOS-only — the decision is simpler than it looks.",
        "date_published": "2026-04-22",
    },
    {
        "file": "src/plumbers/tradify-vs-powered-now.html",
        "canonical": "https://softwaresorted.co.uk/plumbers/tradify-vs-powered-now/",
        "type": "Article",
        "title": "Tradify vs Powered Now: Which Is Better for UK Plumbers? (2026) — SoftwareSorted",
        "description": "Tradify vs Powered Now compared for UK plumbers. Gas Safe certificates, Legionella risk assessments, CIS compliance, offline working, and real pricing — which wins for your business?",
        "date_published": "2026-04-22",
    },
    {
        "file": "src/plumbers/tradify-vs-jobber.html",
        "canonical": "https://softwaresorted.co.uk/plumbers/tradify-vs-jobber/",
        "type": "Article",
        "title": "Tradify vs Jobber: Which Is Better for UK Plumbers? (2026) — SoftwareSorted",
        "description": "Tradify vs Jobber for UK plumbers: pricing, Xero integration, client portal value, and when Jobber's team plan actually makes sense. Real numbers compared.",
        "date_published": "2026-04-22",
    },
    {
        "file": "src/plumbers/servicem8-vs-powered-now.html",
        "canonical": "https://softwaresorted.co.uk/plumbers/servicem8-vs-powered-now/",
        "type": "Article",
        "title": "ServiceM8 vs Powered Now: Which Is Better for UK Plumbers? (2026) — SoftwareSorted",
        "description": "ServiceM8 vs Powered Now for UK plumbers. Gas Safe certificates, Android support, compliance, offline mode, and client automation compared. One tool wins clearly for most.",
        "date_published": "2026-04-22",
    },
    {
        "file": "src/plumbers/job-management-software-gas-safe-water-regs.html",
        "canonical": "https://softwaresorted.co.uk/plumbers/job-management-software-gas-safe-water-regs/",
        "type": "Article",
        "title": "Job Management Software for Gas Safe & Water Regs: Which Tools Handle Compliance? — SoftwareSorted",
        "description": "Which job management software actually handles Gas Safe certificates, CP12 records, Legionella risk assessments, and Water Regulations for UK plumbers? An honest comparison.",
        "date_published": "2026-04-22",
    },
]


def build_schema(page):
    t = page["type"]
    base = {
        "@context": "https://schema.org",
        "@type": t,
        "dateModified": DATE_MODIFIED,
        "url": page["canonical"],
    }
    if t == "WebSite":
        return {**base,
                "name": "SoftwareSorted",
                "description": page["description"],
                "publisher": PUBLISHER}
    elif t == "Review":
        return {**base,
                "headline": page["title"],
                "description": page["description"],
                "itemReviewed": {"@type": "SoftwareApplication", "name": page["item_reviewed"]},
                "author": AUTHOR,
                "publisher": PUBLISHER,
                "datePublished": page["date_published"]}
    else:  # Article
        return {**base,
                "headline": page["title"],
                "description": page["description"],
                "author": AUTHOR,
                "publisher": PUBLISHER,
                "datePublished": page["date_published"]}


def process(page):
    filepath = os.path.join(BASE, page["file"])
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    canonical_tag = f'<link rel="canonical" href="{page["canonical"]}">'
    schema_json   = json.dumps(build_schema(page), indent=2, ensure_ascii=False)
    schema_block  = f'<script type="application/ld+json">\n{schema_json}\n</script>'
    insert_block  = f'{canonical_tag}\n{schema_block}'

    # Strip any pre-existing schema (only the gas safe page has one, but be safe)
    content = re.sub(
        r'\s*<script type="application/ld\+json">.*?</script>',
        "",
        content,
        flags=re.DOTALL,
    )

    # Insert between </style> and </head> (handles blank lines between them)
    new_content = re.sub(
        r"(</style>)\s*(</head>)",
        lambda m: f"{m.group(1)}\n{insert_block}\n{m.group(2)}",
        content,
    )

    if new_content == content:
        print(f"WARN: no insertion point found in {page['file']}")
        return

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"OK  {page['file']}")


if __name__ == "__main__":
    for page in PAGES:
        process(page)
    print(f"\nProcessed {len(PAGES)} pages.")
