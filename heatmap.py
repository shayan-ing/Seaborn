import seaborn as sns

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel("ESD.xlsx")
gp = data.groupby("Job Title").agg({"Annual Salary":"mean"})
sns.heatmap(gp)
plt.show()