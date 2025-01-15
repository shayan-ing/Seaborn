import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data  = pd.read_excel("ESD.xlsx")
# print(data)
sns.stripplot(data=data, x = "Department", y="Age", hue="Gender", dodge=True, jitter=0.4)
plt.legend(bbox_to_anchor=(.8,1))
plt.show()