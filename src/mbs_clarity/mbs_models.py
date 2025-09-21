from enum import Enum

from pydantic import BaseModel


class RelationType(str, Enum):
    EXCLUDES = "excludes"
    SAME_DAY_EXCLUDES = "same_day_excludes"
    ALLOWS_SAME_DAY = "allows_same_day"
    PREREQUISITE = "prerequisite"
    DERIVED_FEE_REF = "derived_fee_ref"
    GENERIC_EXCLUDES = "generic_excludes"


class ConstraintType(str, Enum):
    ONCE_PER_LIFETIME = "once_per_lifetime"
    MAX_PER_12_MONTHS = "max_per_12_months"
    MAX_PER_WINDOW = "max_per_window"  # value like "1/day" or "2/12months"
    COOLDOWN_MONTHS = "cooldown_months"
    COOLDOWN_DAYS = "cooldown_days"
    COOLDOWN_WEEKS = "cooldown_weeks"
    COOLDOWN_YEARS = "cooldown_years"
    SAME_DAY_ONLY = "same_day_only"
    SAME_OCCASION = "same_occasion"
    LOCATION = "location"
    DURATION_MIN_MINUTES = "duration_min_minutes"
    DURATION_MAX_MINUTES = "duration_max_minutes"
    PROVIDER = "provider"
    AGE_MIN_YEARS = "age_min_years"
    AGE_MAX_YEARS = "age_max_years"
    TELEHEALTH = "telehealth"
    REQUIREMENT = "requirement"
    REQUIRES_REFERRAL = "requires_referral"
    INITIAL_ATTENDANCE = "initial_attendance"
    SUBSEQUENT_ATTENDANCE = "subsequent_attendance"
    SINGLE_COURSE = "single_course_of_treatment"


class Item(BaseModel):
    item_num: str
    category: str | None = None
    group_code: str | None = None
    schedule_fee: float | None = None
    description: str | None = None
    derived_fee: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    provider_type: str | None = None
    emsn_description: str | None = None


class Relation(BaseModel):
    item_num: str
    relation_type: RelationType
    target_item_num: str | None = None
    detail: str | None = None


class Constraint(BaseModel):
    item_num: str
    constraint_type: ConstraintType
    value: str


class ItemAggregate(BaseModel):
    item: Item
    relations: list[Relation]
    constraints: list[Constraint]
