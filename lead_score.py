"""
lead_score.py

Handles lead scoring and lead classification.
"""

### SCORING TABLES ###

EXISTING_TECHNOLOGY_SCORES = {

    "none": 20,
    "basic": 15,
    "moderate": 10,
    "advanced": 5,
}

CURRENT_SYSTEM_SCORES = {

    "paper_based": 20,
    "excel": 15,
    "basic_software": 10,
    "modern_sis": 5,
}

DECISION_MAKER_SCORES = {

    "owner": 20,
    "director": 15,
    "principal": 10,
    "admin_staff": 5,
}

INTEREST_LEVEL_SCORES = {

    "requested_demo": 20,
    "requested_proposal": 15,
    "follow_up_needed": 10,
    "neutral": 5,
    "not_interested": 0,
}


### INDIVIDUAL SCORING FUNCTIONS ###
def school_fees_score(fees: int) -> int:
    """
    Return score based on average school fees.
    """
    if fees >= 500_000:
        return 20
    
    if fees >= 300_000:
        return 15
    
    if fees >= 100_000:
        return 10
    
    if fees > 0:
        return 5
    
    return 0


def student_count_score(student_count: int) -> int:
    """
    Return score based on number of students.
    """
    if student_count > 200:
        return 20

    if 100 <= student_count <= 200:
        return 15

    if 50 <= student_count < 100:
        return 10

    if 1 <= student_count < 50:
        return 5

    return 0

### SCORING LOGIC ###
def calculate_score(lead: dict) -> int:
    """
    Calculate and return the total score for a lead.
    """
    total_score = 0

    total_score += EXISTING_TECHNOLOGY_SCORES.get(
        lead.get("existing_technology", "").lower(), 0)
    
    total_score += CURRENT_SYSTEM_SCORES.get(
        lead.get("current_system", "").lower(), 0) 
    
    total_score += DECISION_MAKER_SCORES.get(
        lead.get("decision_maker", "").lower(), 0)
    
    total_score += INTEREST_LEVEL_SCORES.get(
        lead.get("interest_level", "").lower(), 0)
    
    fees = int(lead.get("fees", 0) or 0)
    student_count = int(lead.get("student_count", 0) or 0)

    total_score += school_fees_score(fees)
    total_score += student_count_score(student_count)
    
    return total_score



### LEAD CLASSIFICATION ### 
def classify_lead(total_score: int) -> str:
    """
    Classify each lead based on their total score.
    """
    if total_score >= 100:
        return "Hot Lead"
    
    if total_score >= 75:
        return "Warm Lead"
    
    if total_score >= 50:
        return "Nurture Lead"
    
    return "Low Priority"
    

### LEAD EVALUATION ###
def evaluate_lead(lead: dict) -> tuple[int, str]:
    """
    Evaluate a lead and return its score and status.
    """
    score = calculate_score(lead)
    status = classify_lead(score)

    return score, status






