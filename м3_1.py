from datetime import datetime

def days_until(target_date_str):
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
    current_date = datetime.today()
    difference = (target_date - current_date).days
    
    return difference

print (days_until("2025-01-01"))