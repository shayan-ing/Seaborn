import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("Tips")

sns.boxplot(data=data, x= "day", y = "tip", orient="vertical", fliersize=3,palette="inferno")
plt.show()