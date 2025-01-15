import seaborn as sns

import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("tips")
sns.scatterplot(data = data, x='total_bill',y='tip',hue='day',size='size', marker='D')
plt.show()