import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
# sns.set_style(style="whitegrid")
sns.catplot(x="day", y="tip", data=data, hue="sex", palette="viridis", kind="violin")
plt.show()