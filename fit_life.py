# Проект FitLife - MVP версия 1.0

# константы для расчета нормы воды
WATER_PER_KG = 30
ML_IN_LITER = 1000

# 1. Знакомство
user_name = input('Введите ваше имя: ')
user_name = user_name.title()
user_age = int(input('Введите ваш возраст: '))


# 2. Сбор данных
user_weight = float(input('Введите ваш вес в килограммах: '))
user_height = float(input('Введите ваш рост в метрах через точку (например, 1.68): '))


# 3. Рассчёт bmi (Индекс массы тела)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)


# 4. Рассчёт нормы воды в мл --> л
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_IN_LITER


# 5. Вывод отчёта для пользователя
print(f'''{user_name}, я всё посчитал! Для твоего возраста ({user_age} лет),\n
Твой ИМТ (индекс массы тела) составляет: {bmi}
Старайся пить примерно {water_l:.1f} л воды в день\n''')
print("Расчет окончен. Будьте здоровы!")