import pandas as pd
import numpy as np

def calculate_solar_energy(latitude, longitude, date, panel_power, panel_tilt, panel_azimuth):
    # Здійснюємо розрахунки енергії за годину для заданої дати
    # Реалізацію функції розрахунку можна замінити на виклик зовнішнього сервісу, якщо такий вам підходить

    # Приклад: простий розрахунок для ілюстрації
    solar_constant = 1361  # постійна сонячна константа в Вт/м^2
    latitude_rad = np.radians(latitude)
    day_of_year = date.timetuple().tm_yday

    # Кут сонця над горизонтом
    solar_elevation = 90 - np.degrees(np.arcsin(np.sin(latitude_rad) * np.sin(np.radians(23.45)) +
                                              np.cos(latitude_rad) * np.cos(np.radians(23.45)) *
                                              np.cos(np.radians(15 * (day_of_year - 172)))))

    # Коригування кута нахилу та азимуту
    angle_of_incidence = np.degrees(np.arccos(np.sin(np.radians(panel_tilt)) * np.sin(np.radians(solar_elevation)) +
                                              np.cos(np.radians(panel_tilt)) * np.cos(np.radians(solar_elevation)) *
                                              np.cos(np.radians(panel_azimuth))))

    # Розрахунок ефективної потужності
    effective_power = panel_power * np.sin(np.radians(angle_of_incidence))

    return effective_power

def generate_solar_energy_table(latitude, longitude, start_date, end_date, panel_power, panel_tilt, panel_azimuth):
    # Генеруємо таблицю для заданого періоду
    date_range = pd.date_range(start=start_date, end=end_date, freq='H')
    energy_data = []

    for date in date_range:
        energy = calculate_solar_energy(latitude, longitude, date, panel_power, panel_tilt, panel_azimuth)
        energy_data.append({'Date': date, 'Solar Energy (W)': energy})

    energy_table = pd.DataFrame(energy_data)
    return energy_table

# Зчитуємо введені дані від користувача
latitude = float(input("Введіть широту (градуси): "))
longitude = float(input("Введіть довготу (градуси): "))
start_date = pd.to_datetime(input("Введіть початкову дату у форматі YYYY-MM-DD HH:mm: "))
end_date = pd.to_datetime(input("Введіть кінцеву дату у форматі YYYY-MM-DD HH:mm: "))
panel_power = float(input("Введіть потужність сонячної панелі (Вт): "))
panel_tilt = float(input("Введіть кут нахилу сонячної панелі (градуси): "))
panel_azimuth = float(input("Введіть азимут сонячної панелі (градуси): "))

# Генеруємо таблицю та виводимо результат
energy_table = generate_solar_energy_table(latitude, longitude, start_date, end_date, panel_power, panel_tilt, panel_azimuth)
print(energy_table)
