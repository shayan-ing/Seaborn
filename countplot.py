import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# data = sns.load_dataset("tips")
# sns.countplot(data= data, x="day")
# plt.show()

df=pd.read_excel("ESD.xlsx")
# print(df)
sns.countplot(data=df,x="Department", hue="Gender", palette="viridis")
plt.show()