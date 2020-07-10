import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"./birthYearly.csv")

data = df.pivot('month', 'year', 'births')

sns.set(rc={'figure.figsize':(12,6)})
sns.heatmap(data, annot=True, fmt="d")
plt.show()