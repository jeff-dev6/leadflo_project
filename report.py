"""
report.py

Generates reports
"""


from storage import load_leads




def total_leads() -> int:
    leads = load_leads()
    total_leads = len(leads)
    return total_leads


def total_hot_leads() -> int:
    raw_leads = load_leads()
    hot_leads = [ lead for lead in raw_leads if int(lead.get("score", 0)) >= 100]
    return len(hot_leads)
    
    
def total_warm_leads() -> int:
    raw_leads = load_leads()
    warm_leads = [lead for lead in raw_leads if 75 <= int(lead.get("score", 0)) < 100]
    return len(warm_leads)


def total_nurture_leads():
    raw_leads = load_leads()
    nurture_leads = [lead for lead in raw_leads if 50 <= int(lead.get("score", 0)) < 75]
    return len(nurture_leads)


def total_low_priority_leads():
    raw_leads = load_leads()
    low_priority = [lead for lead in raw_leads if 10 <= int(lead.get("score", 0)) < 50]
    return len(low_priority)


def get_hot_leads():
    leads = load_leads()

    return [lead for lead in leads if int(lead.get("score", 0)) >= 100]



