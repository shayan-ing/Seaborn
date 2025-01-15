import seaborn as sns

import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
print(data)
sns.barplot(data = data, x="day", y="tip", hue="sex", palette="coolwarm", order= ["Sun","Sat","Fri","Thur"])
plt.show()