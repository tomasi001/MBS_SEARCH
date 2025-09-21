import re

from .mbs_models import ConstraintType, RelationType

# Common compiled regex patterns
ITEM_NUMBER = r"\b\d{1,5}\b"
# Matches: item 106, items 106, 109, 125 or 16401
ITEM_LIST_PATTERN = re.compile(
    r"\bitems?\s+((?:"
    + ITEM_NUMBER
    + r"(?:\s*,\s*|\s+or\s+|\s+and\s+))*"
    + ITEM_NUMBER
    + r")",
    re.IGNORECASE,
)
SINGLE_ITEM_PATTERN = re.compile(r"\bitem\s+(" + ITEM_NUMBER + r")", re.IGNORECASE)

# Relationship phrases
EXCLUDE_PHRASES = [
    r"other than a service to which item",
    r"other than a service to which another item applies",
    r"not in association with item",
    r"not claimable with item",
    r"not being a service to which item",
]
SAME_DAY_EXCLUDE_PHRASES = [
    r"not on the same day as item",
    r"must not be performed on the same day as item",
]
ALLOW_SAME_DAY_PHRASES = [
    r"may be claimed on the same day as item",
    r"can be performed on the same day as item",
]
PREREQ_PHRASES = [
    r"after the initial attendance",
    r"following referral",
    r"requires (?:a )?service to which item",
]

# Constraints
ONCE_PER_LIFE = re.compile(r"\bonce per lifetime\b", re.IGNORECASE)
PRECEDING_12_MONTHS = re.compile(r"\bpreceding\s+(\d+)\s+months\b", re.IGNORECASE)
MAX_TIMES_IN_WINDOW = re.compile(
    r"\b(?:no more than|not more than|maximum of)\s+(\d+)\s+(?:times|services?)\s+in\s+(\d+)\s+months\b",
    re.IGNORECASE,
)
SAME_DAY_ONLY = re.compile(r"\bon the same day\b", re.IGNORECASE)
DURATION_MIN = re.compile(r"\bat least\s+(\d+)\s+minutes\b", re.IGNORECASE)
DURATION_MAX = re.compile(r"\bless than\s+(\d+)\s+minutes\b", re.IGNORECASE)
AGE_MIN = re.compile(
    r"\bat least\s+(\d+)\s+years?\b|\baged\s+(\d+)\s+years?\s+or\s+older\b",
    re.IGNORECASE,
)
AGE_MAX = re.compile(
    r"\bunder\s+(\d+)\s+years?\b|\baged\s+(\d+)\s+years?\s+or\s+younger\b",
    re.IGNORECASE,
)
TELEHEALTH = re.compile(r"\btelehealth|video attendance\b", re.IGNORECASE)

LOCATIONS = [
    "consulting rooms",
    "hospital",
    "home",
    "residential aged care facility",
]
PROVIDERS = [
    "general practitioner",
    "specialist",
    "consultant physician",
]


def _extract_item_numbers_around(
    text: str, anchor_index: int, window: int = 120
) -> list[str]:
    start = max(0, anchor_index - window)
    end = min(len(text), anchor_index + window)
    snippet = text[start:end]
    return re.findall(ITEM_NUMBER, snippet)


def _expand_item_list(segment: str) -> list[str]:
    numbers = re.findall(ITEM_NUMBER, segment)
    return list(dict.fromkeys(numbers))


def extract_relations(
    item_num: str, description: str, derived_fee: str | None = None
) -> list[tuple[str, str, str | None, str | None]]:
    relations: list[tuple[str, str, str | None, str | None]] = []
    text = description or ""

    # Exclusions
    for phrase in EXCLUDE_PHRASES:
        for m in re.finditer(phrase, text, re.IGNORECASE):
            targets = _extract_item_numbers_around(text, m.start())
            for t in targets:
                if t != item_num:
                    relations.append((item_num, RelationType.EXCLUDES.value, t, phrase))

    # Same-day exclusions
    for phrase in SAME_DAY_EXCLUDE_PHRASES:
        for m in re.finditer(phrase, text, re.IGNORECASE):
            targets = _extract_item_numbers_around(text, m.start())
            for t in targets:
                if t != item_num:
                    relations.append(
                        (item_num, RelationType.SAME_DAY_EXCLUDES.value, t, phrase)
                    )

    # Same-day allowances
    for phrase in ALLOW_SAME_DAY_PHRASES:
        for m in re.finditer(phrase, text, re.IGNORECASE):
            targets = _extract_item_numbers_around(text, m.start())
            for t in targets:
                if t != item_num:
                    relations.append(
                        (item_num, RelationType.ALLOWS_SAME_DAY.value, t, phrase)
                    )

    # Prerequisites (heuristic)
    for phrase in PREREQ_PHRASES:
        for m in re.finditer(phrase, text, re.IGNORECASE):
            targets = _extract_item_numbers_around(text, m.start())
            for t in targets:
                if t != item_num:
                    relations.append(
                        (item_num, RelationType.PREREQUISITE.value, t, phrase)
                    )

    # Generic item list capture (fallback)
    for m in ITEM_LIST_PATTERN.finditer(text):
        for t in _expand_item_list(m.group(1)):
            if t != item_num:
                relations.append(
                    (item_num, RelationType.EXCLUDES.value, t, "items list")
                )

    # Single item mentions (very conservative)
    for m in SINGLE_ITEM_PATTERN.finditer(text):
        t = m.group(1)
        if t != item_num:
            # Default to excludes unless overridden by other phrases nearby
            relations.append(
                (item_num, RelationType.EXCLUDES.value, t, "single item mention")
            )

    # Derived fee references
    if derived_fee:
        for m in SINGLE_ITEM_PATTERN.finditer(derived_fee):
            t = m.group(1)
            if t != item_num:
                relations.append(
                    (item_num, RelationType.DERIVED_FEE_REF.value, t, "derived fee")
                )

    # De-duplicate
    dedup = list(dict.fromkeys(relations))
    return dedup


def extract_constraints(item_num: str, description: str) -> list[tuple[str, str, str]]:
    constraints: list[tuple[str, str, str]] = []
    text = description or ""

    if ONCE_PER_LIFE.search(text):
        constraints.append((item_num, ConstraintType.ONCE_PER_LIFETIME.value, "true"))

    if m := PRECEDING_12_MONTHS.search(text):
        months = m.group(1)
        constraints.append((item_num, ConstraintType.COOLDOWN_MONTHS.value, months))

    if m := MAX_TIMES_IN_WINDOW.search(text):
        max_times, months = m.group(1), m.group(2)
        if months == "12":
            constraints.append(
                (item_num, ConstraintType.MAX_PER_12_MONTHS.value, max_times)
            )

    if SAME_DAY_ONLY.search(text):
        constraints.append((item_num, ConstraintType.SAME_DAY_ONLY.value, "true"))

    if m := DURATION_MIN.search(text):
        constraints.append(
            (item_num, ConstraintType.DURATION_MIN_MINUTES.value, m.group(1))
        )

    if m := DURATION_MAX.search(text):
        constraints.append(
            (item_num, ConstraintType.DURATION_MAX_MINUTES.value, m.group(1))
        )

    # Locations
    for loc in LOCATIONS:
        if re.search(rf"\b{re.escape(loc)}\b", text, re.IGNORECASE):
            constraints.append((item_num, ConstraintType.LOCATION.value, loc))

    # Provider
    for prov in PROVIDERS:
        if re.search(rf"\b{re.escape(prov)}\b", text, re.IGNORECASE):
            constraints.append((item_num, ConstraintType.PROVIDER.value, prov))

    # Age
    for m in AGE_MIN.finditer(text):
        val = next((g for g in m.groups() if g), None)
        if val:
            constraints.append((item_num, ConstraintType.AGE_MIN_YEARS.value, val))

    for m in AGE_MAX.finditer(text):
        val = next((g for g in m.groups() if g), None)
        if val:
            constraints.append((item_num, ConstraintType.AGE_MAX_YEARS.value, val))

    # Telehealth
    if TELEHEALTH.search(text):
        constraints.append((item_num, ConstraintType.TELEHEALTH.value, "true"))

    # De-duplicate
    constraints = list(dict.fromkeys(constraints))
    return constraints
