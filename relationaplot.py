import seaborn as sns

import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.relplot(data=data,x="tip",y="total_bill", hue="sex", col="day")
plt.show()