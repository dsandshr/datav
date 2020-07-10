import pandas as pd
import matplotlib.pyplot as plt

# Создание таблицы данных, используюя json файл
df = pd.read_json (r'./rain.json') 
print(df)

# Вывод статистики
print("df statistics:", df.describe())

# Создание и вывод графа...
df.plot(x="Month", y = 'Temperature')
plt.show()