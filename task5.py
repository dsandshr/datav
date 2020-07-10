import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"./tempYearly.csv")

sns.set(rc={'figure.figsize':(12,6)})
sns.jointplot('Rainfall', "Temperature", data=df, kind="reg")
plt.show()