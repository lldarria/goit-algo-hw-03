import re

def normalize_phone(phone_number):
    # Видаляємо всі зайві символи, залишаючи лише цифри та '+'
    phone_number = re.sub(r'[^\d+]', '', phone_number.strip())
    
    if phone_number.startswith('+38'):
        return phone_number
    elif phone_number.startswith('+'):
        # Якщо номер починається з '+', додаємо код '+38', але уникаємо дублювання
        return '+38' + phone_number[1:]
    elif phone_number.startswith('380'):
        # Якщо номер починається з '380', додаємо тільки '+'
        return '+' + phone_number
    else:
        # Якщо код країни відсутній, додаємо '+38'
        return '+38' + phone_number

# Тестування функції
print(normalize_phone("    +38(050)123-32-34"))  # +380501233234
print(normalize_phone("     0503451234"))        # +380503451234
print(normalize_phone("(050)8889900"))           # +380508889900
print(normalize_phone("38050-111-22-22"))        # +380501112222
print(normalize_phone("38050 111 22 11   "))     # +380501112211
