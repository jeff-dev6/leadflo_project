import os
import csv
from datetime import datetime



FIELDS = [
    "name",
    "business",
    "email",
    "phone",
    "industry",
    "interest",
    "budget",
    "score",
    "status"
]

HISTORY_FIELDS = [
    "timestamp",
    "action",
    "status"
]

LEADS_FILE = "leads.csv"
HISTORY_FILE = "history.csv"



def get_lead():
    """Dynamically get leads from user"""
    lead = {}

    for field_name in FIELDS:
        prompt = field_name.replace("_", " ")
        lead[field_name] = input(f"Enter lead {prompt}: ").strip()

    return lead



def save_lead(lead):
    """Saves leads to leads.csv"""
    file_exists = os.path.isfile(LEADS_FILE)

    with open(LEADS_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if not file_exists:
            writer.writeheader()

        writer.writerow(lead)



def load_leads():
    """Load all leads from leads.csv."""
    leads = []

    try:
        with open(LEADS_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        return []



def save_history(action, status):
    """Saves activity record to history.csv"""
    history_record = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "status": status
    }

    file_exists = os.path.isfile(HISTORY_FILE)

    with open(HISTORY_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=HISTORY_FIELDS)

        if not file_exists:
            writer.writeheader()

        writer.writerow(history_record)