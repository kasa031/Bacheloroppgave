"""Content for the five ICO site slides (slides 8-12)."""

ART6_HEADING = "Article 6(1) GDPR"
ART6_SUB = "Six lawful bases for processing personal data:"

ART6_BASES = [
    "Consent (a)",
    "Contractual necessity (b)",
    "Legal obligation (c)",
    "Vital interests (d)",
    "Public task (e)",
    "Legitimate interests (f)",
]

SITE_SLIDES = [
    {
        "n": 8,
        "kicker": "Part 2",
        "title": "skatteetaten.no: two purposes",
        "logo": "logo_skatteetaten_no.png",
        "sector": "Government",
        "note": "Two purposes in the notice, two ICO runs. Figure 7 in the report splits the privacy notice from the cookie page.",
        "blocks": [
            {
                "purpose": "Tax and National Population Register data",
                "notice": "The law requires this processing. Opt-out is generally not possible.",
                "ico": "Legal obligation and public task APPROPRIATE. Consent NOT APPROPRIATE.",
                "match": "Yes",
            },
            {
                "purpose": "Optional statistics cookies",
                "notice": "Skyra, Matomo, Google Analytics and Siteimprove. The notice claims consent.",
                "ico": "Consent INCONCLUSIVE. No basis APPROPRIATE.",
                "match": "Partial",
            },
        ],
    },
    {
        "n": 9,
        "kicker": "Part 2",
        "title": "netflix.no: paid streaming",
        "logo": "logo_netflix_com.png",
        "sector": "News / media",
        "note": "One purpose, one basis. Ads and marketing in the same notice were left out.",
        "blocks": [
            {
                "purpose": "Account and payment data for the paid subscription",
                "notice": "EEA/UK privacy statement: contractual necessity to provide the service.",
                "ico": "Contract APPROPRIATE. Consent marked likely invalid for this purpose.",
                "match": "Yes",
            },
        ],
    },
    {
        "n": 10,
        "kicker": "Part 2",
        "title": "fotball.no: match history",
        "logo": "logo_fotball_no.png",
        "sector": "Sport",
        "note": "fotball.no has the highest Webbkoll request count. Contact and lawful basis are separate questions.",
        "blocks": [
            {
                "purpose": "Player name and club on public match history (13+)",
                "notice": "NFF publishes active players with club opt-out. Not a public authority.",
                "ico": "Legitimate interests APPROPRIATE. Public task does not fit.",
                "match": "Yes",
                "extra": "FIKS membership is a different purpose and was not this ICO run.",
            },
        ],
    },
    {
        "n": 11,
        "kicker": "Part 2",
        "title": "document.no: Google Signals",
        "logo": "logo_document_no.png",
        "sector": "News / media",
        "note": "Contract and legitimate interests do not fit this advertising purpose.",
        "blocks": [
            {
                "purpose": "Google Signals advertising analytics",
                "notice": "Article 6 is not named. Collection runs with Google login and ad personalization.",
                "ico": "Consent INCONCLUSIVE. No basis APPROPRIATE.",
                "match": "Partial",
                "extra": "The choice sits in Google settings. Document Pluss terms also bundle the notice.",
            },
        ],
    },
    {
        "n": 12,
        "kicker": "Part 2",
        "title": "babyshop.no: checkout",
        "logo": "logo_babyshop_no.png",
        "sector": "Shopping",
        "note": "Same pattern as Netflix: contract for the core transaction.",
        "blocks": [
            {
                "purpose": "Checkout and order fulfilment",
                "notice": "Name, address, contact, order and payment to deliver goods. Sales terms = purchase contract.",
                "ico": "Contract APPROPRIATE. Article 6(1)(b) is not labeled in the notice.",
                "match": "Yes",
                "extra": "Marketing and profiling stay a separate purpose.",
            },
        ],
    },
]
