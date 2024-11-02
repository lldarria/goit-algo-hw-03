import random

def  get_numbers_ticket(min, max, quantity):
    if not (1 <= min < max <= 1000) or not (1 <= quantity <= (max - min+ 1)):
        return []
    
    # Генерація унікальних випадкових чисел
    unique_numbers = random.sample(range(min, max + 1), quantity)

    # Повернення відсортованого списку
    return sorted(unique_numbers)

print(get_numbers_ticket(1, 100, 5))  
