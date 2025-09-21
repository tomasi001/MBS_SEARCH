import re

from mbs_clarity.mbs_models import ConstraintType, RelationType

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
    r"not in association with item",
    r"not claimable with item",
    r"not being a service to which item",
]
GENERIC_EXCLUDE_PHRASES = [
    r"other than a service to which another item in the table applies",
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
# General windows
MAX_PER_WINDOW = re.compile(
    r"\b(?:no more than|not more than|maximum of)\s+(\d+)\s+(?:times|services?)\s+per\s+(day|week|month|year)\b",
    re.IGNORECASE,
)
ONCE_PER_WINDOW = re.compile(r"\bonce per\s+(day|week|month|year)\b", re.IGNORECASE)
COOLDOWN_GENERIC = re.compile(
    r"\b(?:not within|preceding)\s+(\d+)\s+(days?|weeks?|months?|years?)\b",
    re.IGNORECASE,
)
SAME_OCCASION = re.compile(r"\bsame (?:occasion|visit)\b", re.IGNORECASE)

SAME_DAY_ONLY = re.compile(r"\bon the same day\b", re.IGNORECASE)
DURATION_MIN = re.compile(r"\bat least\s+(\d+)\s+minutes\b", re.IGNORECASE)
DURATION_MAX = re.compile(
    r"\b(?:less than|up to|no more than)\s+(\d+)\s+minutes\b", re.IGNORECASE
)
DURATION_MIN_HOURS = re.compile(r"\bat least\s+(\d+)\s+hours?\b", re.IGNORECASE)
DURATION_RANGE_MINMAX = re.compile(
    r"\b(\d+)\s*(?:to|-|–)\s*(\d+)\s+minutes\b", re.IGNORECASE
)
DURATION_EXACT_HOURS = re.compile(r"\b(\d+)\s+hours?\b", re.IGNORECASE)

# Additional duration patterns
DURATION_APPROXIMATE = re.compile(
    r"\bapproximately\s+(\d+)\s+minutes?\b", re.IGNORECASE
)
DURATION_ABOUT = re.compile(r"\babout\s+(\d+)\s+minutes?\b", re.IGNORECASE)
DURATION_OR_MORE = re.compile(r"\b(\d+)\s+minutes?\s+or\s+more\b", re.IGNORECASE)
DURATION_OR_LESS = re.compile(r"\b(\d+)\s+minutes?\s+or\s+less\b", re.IGNORECASE)

# Additional frequency patterns
EVERY_X_PERIOD = re.compile(
    r"\bevery\s+(\d+)\s+(day|week|month|year)s?\b", re.IGNORECASE
)
NOT_MORE_THAN_X_PER_YEAR = re.compile(
    r"\bnot more than\s+(\d+)\s+(?:times|services?)\s+per\s+year\b", re.IGNORECASE
)
NOT_MORE_THAN_X_PER_MONTH = re.compile(
    r"\bnot more than\s+(\d+)\s+(?:times|services?)\s+per\s+month\b", re.IGNORECASE
)
NOT_MORE_THAN_X_PER_WEEK = re.compile(
    r"\bnot more than\s+(\d+)\s+(?:times|services?)\s+per\s+week\b", re.IGNORECASE
)
NOT_MORE_THAN_X_PER_DAY = re.compile(
    r"\bnot more than\s+(\d+)\s+(?:times|services?)\s+per\s+day\b", re.IGNORECASE
)

# Additional cooldown patterns
WITHIN_X_PERIOD = re.compile(
    r"\bwithin\s+(\d+)\s+(days?|weeks?|months?|years?)\b", re.IGNORECASE
)
AFTER_X_PERIOD = re.compile(
    r"\bafter\s+(\d+)\s+(days?|weeks?|months?|years?)\b", re.IGNORECASE
)

AGE_MIN = re.compile(
    r"\bat least\s+(\d+)\s+years?\b|\baged\s+(\d+)\s+years?\s+or\s+older\b",
    re.IGNORECASE,
)
AGE_MAX = re.compile(
    r"\bunder\s+(\d+)\s+years?\b|\baged\s+(\d+)\s+years?\s+or\s+younger\b",
    re.IGNORECASE,
)
TELEHEALTH = re.compile(r"\btelehealth|video attendance\b", re.IGNORECASE)

# Lettered clauses like (a) text; (b) text;
LETTERED_CLAUSES = re.compile(r"\(([a-z])\)\s*([^;\n]+)[;\n]", re.IGNORECASE)

LOCATIONS = [
    "consulting rooms",
    "hospital",
    "home",
    "residential aged care facility",
    "emergency department",
    "intensive care unit",
    "icu",
    "theatre",
    "outpatient",
    "inpatient",
    "clinic",
    "medical centre",
    "general practice",
    "specialist rooms",
    "day surgery",
    "day procedure unit",
    "recovery room",
    "ward",
    "private hospital",
    "public hospital",
    "community health centre",
    "mental health facility",
    "rehabilitation centre",
    "palliative care unit",
    "maternity ward",
    "paediatric ward",
    "cardiac unit",
    "neurology unit",
    "oncology unit",
    "radiology department",
    "pathology laboratory",
    "pharmacy",
    "dental surgery",
    "physiotherapy clinic",
    "occupational therapy",
    "speech therapy",
    "dietitian clinic",
    "psychology clinic",
    "counselling centre",
    "telehealth",
    "video consultation",
    "phone consultation",
    "remote consultation",
]
PROVIDERS = [
    "general practitioner",
    "specialist",
    "consultant physician",
    "medical practitioner",
    "practice nurse",
    "gp registrar",
    "diagnostic radiologist",
    "surgeon",
    "anaesthetist",
    "psychiatrist",
    "psychologist",
    "physiotherapist",
    "occupational therapist",
    "speech therapist",
    "dietitian",
    "pharmacist",
    "dentist",
    "dental specialist",
    "nurse practitioner",
    "midwife",
    "mental health nurse",
    "community health nurse",
    "palliative care nurse",
    "oncology nurse",
    "cardiac nurse",
    "diabetes educator",
    "social worker",
    "counsellor",
    "mental health worker",
    "allied health professional",
    "health professional",
    "healthcare professional",
    "medical specialist",
    "surgical specialist",
    "paediatrician",
    "geriatrician",
    "cardiologist",
    "neurologist",
    "oncologist",
    "dermatologist",
    "ophthalmologist",
    "orthopaedic surgeon",
    "plastic surgeon",
    "neurosurgeon",
    "cardiothoracic surgeon",
    "urologist",
    "gynaecologist",
    "obstetrician",
    "endocrinologist",
    "gastroenterologist",
    "respiratory physician",
    "rheumatologist",
    "nephrologist",
    "haematologist",
    "pathologist",
    "radiologist",
    "nuclear medicine physician",
    "emergency physician",
    "intensive care physician",
    "palliative care physician",
    "rehabilitation physician",
    "sports physician",
    "occupational physician",
    "public health physician",
    "forensic physician",
    "medical officer",
    "resident medical officer",
    "registrar",
    "resident",
    "intern",
    "medical student",
    "nursing student",
    "allied health student",
]

REFERRAL = re.compile(r"\bfollowing referral|valid referral|referral\b", re.IGNORECASE)
INITIAL_ATT = re.compile(r"\binitial attendance\b", re.IGNORECASE)
SUBSEQUENT_ATT = re.compile(r"\bsubsequent attendance\b", re.IGNORECASE)
COURSE = re.compile(r"\bsingle course of treatment\b", re.IGNORECASE)

# Additional referral/course patterns
REFERRAL_REQUIRED = re.compile(
    r"\breferral required|requires referral|must be referred\b", re.IGNORECASE
)
SPECIALIST_REFERRAL = re.compile(
    r"\breferral required from specialist|specialist referral|referral to specialist\b",
    re.IGNORECASE,
)
GP_REFERRAL = re.compile(
    r"\bgp referral|referral from gp|general practitioner referral|must be referred from gp\b",
    re.IGNORECASE,
)
TREATMENT_PLAN = re.compile(r"\btreatment plan|management plan\b", re.IGNORECASE)
CONTINUING_TREATMENT = re.compile(
    r"\bcontinuing treatment|ongoing treatment\b", re.IGNORECASE
)
FIRST_VISIT = re.compile(
    r"\bfirst visit|first attendance|initial visit\b", re.IGNORECASE
)
FOLLOW_UP = re.compile(r"\bfollow.?up|follow.?up visit\b", re.IGNORECASE)


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

    # Specific exclusions referencing concrete items
    for phrase in EXCLUDE_PHRASES:
        for m in re.finditer(phrase, text, re.IGNORECASE):
            targets = _extract_item_numbers_around(text, m.start())
            for t in targets:
                if t != item_num:
                    relations.append((item_num, RelationType.EXCLUDES.value, t, phrase))

    # Generic exclusion (no explicit item number)
    for phrase in GENERIC_EXCLUDE_PHRASES:
        if re.search(phrase, text, re.IGNORECASE):
            relations.append(
                (item_num, RelationType.GENERIC_EXCLUDES.value, None, phrase)
            )

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


def _minutes_from_hours(text_val: str) -> int:
    try:
        return int(text_val) * 60
    except Exception:
        return 0


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

    # General frequency windows
    for m in MAX_PER_WINDOW.finditer(text):
        count, unit = m.group(1), m.group(2).lower()
        constraints.append(
            (item_num, ConstraintType.MAX_PER_WINDOW.value, f"{count}/{unit}")
        )
    for m in ONCE_PER_WINDOW.finditer(text):
        unit = m.group(1).lower()
        constraints.append((item_num, ConstraintType.MAX_PER_WINDOW.value, f"1/{unit}"))

    # Generic cooldowns
    for m in COOLDOWN_GENERIC.finditer(text):
        amount = m.group(1)
        unit = m.group(2).lower()
        if unit.startswith("day"):
            constraints.append((item_num, ConstraintType.COOLDOWN_DAYS.value, amount))
        elif unit.startswith("week"):
            constraints.append((item_num, ConstraintType.COOLDOWN_WEEKS.value, amount))
        elif unit.startswith("month"):
            constraints.append((item_num, ConstraintType.COOLDOWN_MONTHS.value, amount))
        elif unit.startswith("year"):
            constraints.append((item_num, ConstraintType.COOLDOWN_YEARS.value, amount))

    if SAME_DAY_ONLY.search(text):
        constraints.append((item_num, ConstraintType.SAME_DAY_ONLY.value, "true"))

    if SAME_OCCASION.search(text):
        constraints.append((item_num, ConstraintType.SAME_OCCASION.value, "true"))

    # Duration parsing
    if m := DURATION_RANGE_MINMAX.search(text):
        minm, maxm = m.group(1), m.group(2)
        constraints.append((item_num, ConstraintType.DURATION_MIN_MINUTES.value, minm))
        constraints.append((item_num, ConstraintType.DURATION_MAX_MINUTES.value, maxm))

    if m := DURATION_MIN.search(text):
        constraints.append(
            (item_num, ConstraintType.DURATION_MIN_MINUTES.value, m.group(1))
        )

    # Hours-based
    for m in DURATION_MIN_HOURS.finditer(text):
        constraints.append(
            (
                item_num,
                ConstraintType.DURATION_MIN_MINUTES.value,
                str(_minutes_from_hours(m.group(1))),
            )
        )
    # Exact hours mention without min - use as min for safety
    for m in DURATION_EXACT_HOURS.finditer(text):
        constraints.append(
            (
                item_num,
                ConstraintType.DURATION_MIN_MINUTES.value,
                str(_minutes_from_hours(m.group(1))),
            )
        )

    if m := DURATION_MAX.search(text):
        constraints.append(
            (item_num, ConstraintType.DURATION_MAX_MINUTES.value, m.group(1))
        )

    # Additional duration patterns
    for m in DURATION_APPROXIMATE.finditer(text):
        constraints.append(
            (item_num, ConstraintType.DURATION_MIN_MINUTES.value, m.group(1))
        )
    for m in DURATION_ABOUT.finditer(text):
        constraints.append(
            (item_num, ConstraintType.DURATION_MIN_MINUTES.value, m.group(1))
        )
    for m in DURATION_OR_MORE.finditer(text):
        constraints.append(
            (item_num, ConstraintType.DURATION_MIN_MINUTES.value, m.group(1))
        )
    for m in DURATION_OR_LESS.finditer(text):
        constraints.append(
            (item_num, ConstraintType.DURATION_MAX_MINUTES.value, m.group(1))
        )

    # Additional frequency patterns
    for m in EVERY_X_PERIOD.finditer(text):
        count, unit = m.group(1), m.group(2).lower()
        # Convert "every X days" to "1/X days" frequency
        if unit == "day" and count != "1":
            # Every 7 days = 1/week, every 14 days = 1/2weeks, etc.
            if count == "7":
                constraints.append(
                    (item_num, ConstraintType.MAX_PER_WINDOW.value, "1/week")
                )
            elif count == "14":
                constraints.append(
                    (item_num, ConstraintType.MAX_PER_WINDOW.value, "1/2weeks")
                )
            else:
                constraints.append(
                    (item_num, ConstraintType.MAX_PER_WINDOW.value, f"1/{count}days")
                )
        else:
            constraints.append(
                (item_num, ConstraintType.MAX_PER_WINDOW.value, f"1/{unit}")
            )
    for m in NOT_MORE_THAN_X_PER_YEAR.finditer(text):
        count = m.group(1)
        constraints.append(
            (item_num, ConstraintType.MAX_PER_WINDOW.value, f"{count}/year")
        )
    for m in NOT_MORE_THAN_X_PER_MONTH.finditer(text):
        count = m.group(1)
        constraints.append(
            (item_num, ConstraintType.MAX_PER_WINDOW.value, f"{count}/month")
        )
    for m in NOT_MORE_THAN_X_PER_WEEK.finditer(text):
        count = m.group(1)
        constraints.append(
            (item_num, ConstraintType.MAX_PER_WINDOW.value, f"{count}/week")
        )
    for m in NOT_MORE_THAN_X_PER_DAY.finditer(text):
        count = m.group(1)
        constraints.append(
            (item_num, ConstraintType.MAX_PER_WINDOW.value, f"{count}/day")
        )

    # Additional cooldown patterns
    for m in WITHIN_X_PERIOD.finditer(text):
        amount = m.group(1)
        unit = m.group(2).lower()
        if unit.startswith("day"):
            constraints.append((item_num, ConstraintType.COOLDOWN_DAYS.value, amount))
        elif unit.startswith("week"):
            constraints.append((item_num, ConstraintType.COOLDOWN_WEEKS.value, amount))
        elif unit.startswith("month"):
            constraints.append((item_num, ConstraintType.COOLDOWN_MONTHS.value, amount))
        elif unit.startswith("year"):
            constraints.append((item_num, ConstraintType.COOLDOWN_YEARS.value, amount))
    for m in AFTER_X_PERIOD.finditer(text):
        amount = m.group(1)
        unit = m.group(2).lower()
        if unit.startswith("day"):
            constraints.append((item_num, ConstraintType.COOLDOWN_DAYS.value, amount))
        elif unit.startswith("week"):
            constraints.append((item_num, ConstraintType.COOLDOWN_WEEKS.value, amount))
        elif unit.startswith("month"):
            constraints.append((item_num, ConstraintType.COOLDOWN_MONTHS.value, amount))
        elif unit.startswith("year"):
            constraints.append((item_num, ConstraintType.COOLDOWN_YEARS.value, amount))

    # Locations
    for loc in LOCATIONS:
        if re.search(rf"\b{re.escape(loc)}\b", text, re.IGNORECASE):
            constraints.append((item_num, ConstraintType.LOCATION.value, loc))

    # Provider
    for prov in PROVIDERS:
        if re.search(rf"\b{re.escape(prov)}\b", text, re.IGNORECASE):
            constraints.append((item_num, ConstraintType.PROVIDER.value, prov))

    # Lettered requirement clauses (a), (b), ...
    for m in LETTERED_CLAUSES.finditer(text):
        letter = m.group(1).lower()
        clause = m.group(2).strip()
        if clause:
            constraints.append(
                (item_num, ConstraintType.REQUIREMENT.value, f"({letter}) {clause}")
            )

    # Referral/course flags
    if REFERRAL.search(text):
        constraints.append((item_num, ConstraintType.REQUIRES_REFERRAL.value, "true"))
    if INITIAL_ATT.search(text):
        constraints.append((item_num, ConstraintType.INITIAL_ATTENDANCE.value, "true"))
    if SUBSEQUENT_ATT.search(text):
        constraints.append(
            (item_num, ConstraintType.SUBSEQUENT_ATTENDANCE.value, "true")
        )
    if COURSE.search(text):
        constraints.append((item_num, ConstraintType.SINGLE_COURSE.value, "true"))

    # Additional referral/course patterns
    if REFERRAL_REQUIRED.search(text):
        constraints.append((item_num, ConstraintType.REQUIRES_REFERRAL.value, "true"))
    if SPECIALIST_REFERRAL.search(text):
        constraints.append(
            (item_num, ConstraintType.REQUIRES_REFERRAL.value, "specialist")
        )
    if GP_REFERRAL.search(text):
        constraints.append((item_num, ConstraintType.REQUIRES_REFERRAL.value, "gp"))
    if TREATMENT_PLAN.search(text):
        constraints.append(
            (item_num, ConstraintType.REQUIREMENT.value, "treatment plan required")
        )
    if CONTINUING_TREATMENT.search(text):
        constraints.append(
            (item_num, ConstraintType.REQUIREMENT.value, "continuing treatment")
        )
    if FIRST_VISIT.search(text):
        constraints.append((item_num, ConstraintType.INITIAL_ATTENDANCE.value, "true"))
    if FOLLOW_UP.search(text):
        constraints.append(
            (item_num, ConstraintType.SUBSEQUENT_ATTENDANCE.value, "true")
        )

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
