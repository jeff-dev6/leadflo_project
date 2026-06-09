import re

def validate_email(email):

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else: 
        return False
    
    
def phone_number(number):
    pattern = r'^\+?[0-9]{7,15}$'

    if re.match(pattern, number):
        return True
    else:
        return False
    

def clean_text(text):
    return "".join(text.strip().title().split())
        

