"""
Validator.py

Provides functions for validating and cleaning user input.
"""

import re


def validate_email(email: str) -> bool: 
    """
    Checks whether an email address is valid.
    """

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return bool(re.match(pattern, email))

    

def validate_phone_number(number: str) -> bool:
    """
    Checks whether a phone number is valid.
    """
    pattern = r'^\+?[0-9]{7,15}$'

    return bool(re.match(pattern, number))

    

def clean_text(text: str) -> str:
    """
    Clean and format text input.
    """
    return " ".join(text.strip().title().split())
        

