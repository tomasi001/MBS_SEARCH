from mbs_clarity.relationship_extraction import extract_constraints, extract_relations


def test_same_day_exclusion():
    text = "not on the same day as item 36"
    rels = extract_relations("23", text)
    assert ("23", "same_day_excludes", "36", "not on the same day as item") in rels


def test_exclusion_items_list():
    text = "other than a service to which item 106, 109, 125 or 16401 applies"
    rels = extract_relations("104", text)
    expected = {
        ("104", "excludes", "106", "items list"),
        ("104", "excludes", "109", "items list"),
        ("104", "excludes", "125", "items list"),
        ("104", "excludes", "16401", "items list"),
    }
    assert expected.issubset(set(rels))


def test_duration_constraints():
    text = "lasting at least 6 minutes and less than 20 minutes"
    cons = extract_constraints("23", text)
    assert ("23", "duration_min_minutes", "6") in cons
    assert ("23", "duration_max_minutes", "20") in cons


def test_duration_hours_and_range():
    text = "lasting at least 1 hour and 45–60 minutes for certain components"
    cons = extract_constraints("200", text)
    assert ("200", "duration_min_minutes", "60") in cons
    assert ("200", "duration_min_minutes", "45") in cons
    assert ("200", "duration_max_minutes", "60") in cons


def test_frequency_and_cooldowns():
    text = "no more than 2 services per month; once per week; not within 12 months; preceding 14 days"
    cons = extract_constraints("300", text)
    assert ("300", "max_per_window", "2/month") in cons
    assert ("300", "max_per_window", "1/week") in cons
    assert ("300", "cooldown_months", "12") in cons
    assert ("300", "cooldown_days", "14") in cons


def test_referral_and_same_occasion_and_locations():
    text = "following referral in a single course of treatment on the same occasion in emergency department by a medical practitioner"
    cons = extract_constraints("400", text)
    assert ("400", "requires_referral", "true") in cons
    assert ("400", "single_course_of_treatment", "true") in cons
    assert ("400", "same_occasion", "true") in cons
    assert ("400", "location", "emergency department") in cons
    assert ("400", "provider", "medical practitioner") in cons


def test_additional_duration_patterns():
    """Test additional duration patterns."""
    text = "approximately 30 minutes, about 45 minutes, 20 minutes or more, 60 minutes or less"
    cons = extract_constraints("500", text)
    assert ("500", "duration_min_minutes", "30") in cons
    assert ("500", "duration_min_minutes", "45") in cons
    assert ("500", "duration_min_minutes", "20") in cons
    assert ("500", "duration_max_minutes", "60") in cons


def test_additional_frequency_patterns():
    """Test additional frequency patterns."""
    text = "every 7 days, not more than 3 times per year, not more than 2 services per month, not more than 1 time per week, not more than 4 times per day"
    cons = extract_constraints("600", text)
    assert ("600", "max_per_window", "1/week") in cons  # every 7 days -> 1/week
    assert ("600", "max_per_window", "3/year") in cons
    assert ("600", "max_per_window", "2/month") in cons
    assert ("600", "max_per_window", "1/week") in cons
    assert ("600", "max_per_window", "4/day") in cons


def test_additional_cooldown_patterns():
    """Test additional cooldown patterns."""
    text = "within 14 days, within 2 weeks, within 6 months, within 1 year, after 7 days, after 3 weeks, after 12 months, after 2 years"
    cons = extract_constraints("700", text)
    assert ("700", "cooldown_days", "14") in cons
    assert ("700", "cooldown_weeks", "2") in cons
    assert ("700", "cooldown_months", "6") in cons
    assert ("700", "cooldown_years", "1") in cons
    assert ("700", "cooldown_days", "7") in cons
    assert ("700", "cooldown_weeks", "3") in cons
    assert ("700", "cooldown_months", "12") in cons
    assert ("700", "cooldown_years", "2") in cons


def test_complex_duration_and_frequency_combinations():
    """Test complex combinations of duration and frequency patterns."""
    text = "lasting approximately 40 minutes, not more than 2 services per month, within 30 days of previous service, every 14 days"
    cons = extract_constraints("800", text)
    assert ("800", "duration_min_minutes", "40") in cons
    assert ("800", "max_per_window", "2/month") in cons
    assert ("800", "cooldown_days", "30") in cons
    assert ("800", "max_per_window", "1/2weeks") in cons  # every 14 days -> 1/2weeks


def test_additional_referral_course_patterns():
    """Test additional referral and course patterns."""
    text = "referral required from specialist, gp referral needed, treatment plan required, continuing treatment, first visit only, follow-up visit"
    cons = extract_constraints("900", text)
    assert ("900", "requires_referral", "true") in cons
    assert ("900", "requires_referral", "specialist") in cons
    assert ("900", "requires_referral", "gp") in cons
    assert ("900", "requirement", "treatment plan required") in cons
    assert ("900", "requirement", "continuing treatment") in cons
    assert ("900", "initial_attendance", "true") in cons
    assert ("900", "subsequent_attendance", "true") in cons


def test_referral_specificity():
    """Test that different referral types are captured correctly."""
    text = "requires specialist referral, must be referred from gp, referral to specialist required"
    cons = extract_constraints("1000", text)
    assert ("1000", "requires_referral", "specialist") in cons
    assert ("1000", "requires_referral", "gp") in cons
    assert ("1000", "requires_referral", "true") in cons


def test_visit_type_patterns():
    """Test different visit type patterns."""
    text = "first attendance only, subsequent attendance, initial visit, follow-up visit, ongoing treatment"
    cons = extract_constraints("1100", text)
    assert ("1100", "initial_attendance", "true") in cons
    assert ("1100", "subsequent_attendance", "true") in cons
    assert ("1100", "requirement", "continuing treatment") in cons


def test_expanded_locations():
    """Test expanded location patterns."""
    text = "in the emergency department, at home, in consulting rooms, at the clinic, in the hospital, in specialist rooms, at the medical centre, in day surgery, in the ward, at the community health centre, in the mental health facility, at the rehabilitation centre, in the palliative care unit, in the maternity ward, in the paediatric ward, in the cardiac unit, in the neurology unit, in the oncology unit, in the radiology department, in the pathology laboratory, at the pharmacy, in the dental surgery, at the physiotherapy clinic, in occupational therapy, in speech therapy, at the dietitian clinic, at the psychology clinic, at the counselling centre, via telehealth, video consultation, phone consultation, remote consultation"
    cons = extract_constraints("1200", text)

    # Test a subset of the locations
    location_values = [c[2] for c in cons if c[1] == "location"]
    assert "emergency department" in location_values
    assert "home" in location_values
    assert "consulting rooms" in location_values
    assert "clinic" in location_values
    assert "hospital" in location_values
    assert "specialist rooms" in location_values
    assert "medical centre" in location_values
    assert "day surgery" in location_values
    assert "ward" in location_values
    assert "community health centre" in location_values
    assert "mental health facility" in location_values
    assert "rehabilitation centre" in location_values
    assert "palliative care unit" in location_values
    assert "maternity ward" in location_values
    assert "paediatric ward" in location_values
    assert "cardiac unit" in location_values
    assert "neurology unit" in location_values
    assert "oncology unit" in location_values
    assert "radiology department" in location_values
    assert "pathology laboratory" in location_values
    assert "pharmacy" in location_values
    assert "dental surgery" in location_values
    assert "physiotherapy clinic" in location_values
    assert "occupational therapy" in location_values
    assert "speech therapy" in location_values
    assert "dietitian clinic" in location_values
    assert "psychology clinic" in location_values
    assert "counselling centre" in location_values
    assert "telehealth" in location_values
    assert "video consultation" in location_values
    assert "phone consultation" in location_values
    assert "remote consultation" in location_values


def test_expanded_providers():
    """Test expanded provider patterns."""
    text = "by a general practitioner, by a specialist, by a consultant physician, by a medical practitioner, by a practice nurse, by a gp registrar, by a diagnostic radiologist, by a surgeon, by an anaesthetist, by a psychiatrist, by a psychologist, by a physiotherapist, by an occupational therapist, by a speech therapist, by a dietitian, by a pharmacist, by a dentist, by a dental specialist, by a nurse practitioner, by a midwife, by a mental health nurse, by a community health nurse, by a palliative care nurse, by an oncology nurse, by a cardiac nurse, by a diabetes educator, by a social worker, by a counsellor, by a mental health worker, by an allied health professional, by a health professional, by a healthcare professional, by a medical specialist, by a surgical specialist, by a paediatrician, by a geriatrician, by a cardiologist, by a neurologist, by an oncologist, by a dermatologist, by an ophthalmologist, by an orthopaedic surgeon, by a plastic surgeon, by a neurosurgeon, by a cardiothoracic surgeon, by a urologist, by a gynaecologist, by an obstetrician, by an endocrinologist, by a gastroenterologist, by a respiratory physician, by a rheumatologist, by a nephrologist, by a haematologist, by a pathologist, by a radiologist, by a nuclear medicine physician, by an emergency physician, by an intensive care physician, by a palliative care physician, by a rehabilitation physician, by a sports physician, by an occupational physician, by a public health physician, by a forensic physician, by a medical officer, by a resident medical officer, by a registrar, by a resident, by an intern, by a medical student, by a nursing student, by an allied health student"
    cons = extract_constraints("1300", text)

    # Test a subset of the providers
    provider_values = [c[2] for c in cons if c[1] == "provider"]
    assert "general practitioner" in provider_values
    assert "specialist" in provider_values
    assert "consultant physician" in provider_values
    assert "medical practitioner" in provider_values
    assert "practice nurse" in provider_values
    assert "gp registrar" in provider_values
    assert "diagnostic radiologist" in provider_values
    assert "surgeon" in provider_values
    assert "anaesthetist" in provider_values
    assert "psychiatrist" in provider_values
    assert "psychologist" in provider_values
    assert "physiotherapist" in provider_values
    assert "occupational therapist" in provider_values
    assert "speech therapist" in provider_values
    assert "dietitian" in provider_values
    assert "pharmacist" in provider_values
    assert "dentist" in provider_values
    assert "dental specialist" in provider_values
    assert "nurse practitioner" in provider_values
    assert "midwife" in provider_values
    assert "mental health nurse" in provider_values
    assert "community health nurse" in provider_values
    assert "palliative care nurse" in provider_values
    assert "oncology nurse" in provider_values
    assert "cardiac nurse" in provider_values
    assert "diabetes educator" in provider_values
    assert "social worker" in provider_values
    assert "counsellor" in provider_values
    assert "mental health worker" in provider_values
    assert "allied health professional" in provider_values
    assert "health professional" in provider_values
    assert "healthcare professional" in provider_values
    assert "medical specialist" in provider_values
    assert "surgical specialist" in provider_values
    assert "paediatrician" in provider_values
    assert "geriatrician" in provider_values
    assert "cardiologist" in provider_values
    assert "neurologist" in provider_values
    assert "oncologist" in provider_values
    assert "dermatologist" in provider_values
    assert "ophthalmologist" in provider_values
    assert "orthopaedic surgeon" in provider_values
    assert "plastic surgeon" in provider_values
    assert "neurosurgeon" in provider_values
    assert "cardiothoracic surgeon" in provider_values
    assert "urologist" in provider_values
    assert "gynaecologist" in provider_values
    assert "obstetrician" in provider_values
    assert "endocrinologist" in provider_values
    assert "gastroenterologist" in provider_values
    assert "respiratory physician" in provider_values
    assert "rheumatologist" in provider_values
    assert "nephrologist" in provider_values
    assert "haematologist" in provider_values
    assert "pathologist" in provider_values
    assert "radiologist" in provider_values
    assert "nuclear medicine physician" in provider_values
    assert "emergency physician" in provider_values
    assert "intensive care physician" in provider_values
    assert "palliative care physician" in provider_values
    assert "rehabilitation physician" in provider_values
    assert "sports physician" in provider_values
    assert "occupational physician" in provider_values
    assert "public health physician" in provider_values
    assert "forensic physician" in provider_values
    assert "medical officer" in provider_values
    assert "resident medical officer" in provider_values
    assert "registrar" in provider_values
    assert "resident" in provider_values
    assert "intern" in provider_values
    assert "medical student" in provider_values
    assert "nursing student" in provider_values
    assert "allied health student" in provider_values


def test_location_provider_combinations():
    """Test combinations of locations and providers."""
    text = "in the emergency department by an emergency physician, at home by a community health nurse, in consulting rooms by a general practitioner, at the clinic by a physiotherapist, in the hospital by a surgeon, in specialist rooms by a cardiologist, at the medical centre by a practice nurse, in day surgery by an anaesthetist, in the ward by a nursing student, at the community health centre by a social worker"
    cons = extract_constraints("1400", text)

    # Test that both locations and providers are captured
    location_values = [c[2] for c in cons if c[1] == "location"]
    provider_values = [c[2] for c in cons if c[1] == "provider"]

    assert "emergency department" in location_values
    assert "home" in location_values
    assert "consulting rooms" in location_values
    assert "clinic" in location_values
    assert "hospital" in location_values
    assert "specialist rooms" in location_values
    assert "medical centre" in location_values
    assert "day surgery" in location_values
    assert "ward" in location_values
    assert "community health centre" in location_values

    assert "emergency physician" in provider_values
    assert "community health nurse" in provider_values
    assert "general practitioner" in provider_values
    assert "physiotherapist" in provider_values
    assert "surgeon" in provider_values
    assert "cardiologist" in provider_values
    assert "practice nurse" in provider_values
    assert "anaesthetist" in provider_values
    assert "nursing student" in provider_values
    assert "social worker" in provider_values
