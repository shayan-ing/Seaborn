import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data  = pd.read_excel("ESD.xlsx")
sns.pairplot(data,palette="plasma",hue="Annual Salary")
plt.show()