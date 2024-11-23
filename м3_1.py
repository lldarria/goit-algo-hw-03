from datetime import datetime

def get_days_from_today(date_str):
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        difference = (current_date - target_date).days
        return difference
    except ValueError:
        return "Error: Invalid date format. Please use 'YYYY-MM-DD'."

print(get_days_from_today("2025-01-01"))  # Від'ємне число (майбутня дата)
print(get_days_from_today("2020-01-01"))  # Додатне число (минуле)
print(get_days_from_today("2024-11-23"))  # 0 (поточна дата)
print(get_days_from_today("12.2.2000"))   # Повідомлення про помилку
