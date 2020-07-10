import pandas as pd
import matplotlib.pyplot as plt

# Создание таблицы данных
df = pd.read_json(r"./rain.json")

#plt.figure(figsize=(12,5))
#plt.plot(df['Month'], df['Temperature'], label = 'Temperature')
#plt.show()


plt.figure(figsize=(13,5)) # Размер окна
#plt.plot(df['Month'], df['Rainfall'], label = 'Rainfall')
#plt.show()

# Измерение нескольких объектов на диаграмме
plt.plot(df['Month'], df['Rainfall'], label = 'Rainfall')
plt.plot(df['Month'], df['Temperature'], label = 'Temperature')
plt.legend()
plt.show()