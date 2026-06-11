"""
storage.py

Handles storage.
"""

import os
import csv
from datetime import datetime

### CSV FIELDS ###
INPUT_FIELDS = [

    "school_name",
    "contact_person",
    "phone",
    "email",
    "fees",
    "student_count",
    "existing_technology",
    "current_system",
    "decision_maker",
    "interest_level",
]

FIELDS = INPUT_FIELDS + [
    "score",
    "status",
]


HISTORY_FIELDS = [
    "timestamp",
    "action",
    "status"
]


### FILE CONFIGURATION ###
LEADS_FILE = "leads.csv"

HISTORY_FILE = "history.csv"

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"




def get_lead() -> dict[str, str]:
    """
    Prompt the user for lead information and return it as a dictionary.
    """

    lead = {}

    for field_name in INPUT_FIELDS:
        prompt = field_name.replace("_", " ")
        lead[field_name] = input(f"Enter lead {prompt}: ").strip()

    return lead



def save_lead(lead: dict[str, str]) -> None:
    """
    Save a lead record to the leads CSV file.
    """

    file_exists = os.path.isfile(LEADS_FILE)

    with open(LEADS_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if not file_exists:
            writer.writeheader()

        writer.writerow(lead)



def load_leads() -> list[dict[str, str]]:
    """
    Load all lead records from the CSV file.
    """

    try:
        with open(LEADS_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        return []



def save_history(action: str, status: str) -> None:
    """
    Save an activity record to the history CSV file.
    """
    
    history_record = {
        "timestamp": datetime.now().strftime(TIMESTAMP_FORMAT),
        "action": action,
        "status": status
    }

    file_exists = os.path.isfile(HISTORY_FILE)

    with open(HISTORY_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=HISTORY_FIELDS)

        if not file_exists:
            writer.writeheader()

        writer.writerow(history_record)