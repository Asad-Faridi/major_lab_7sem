readings = [22.5, 23.1, 20.9, 24.0,21.5, 19.8, 26.2, 23.5]
fahrenheit_readings=[1.8*i+32 for i in readings]
hot_days=[i for i in readings if i>23.0]
print(fahrenheit_readings)
print(hot_days)