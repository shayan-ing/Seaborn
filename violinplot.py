import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data  = pd.read_excel("ESD.xlsx")
sns.violinplot(data= data, x="Annual Salary",palette="magma")
plt.show()