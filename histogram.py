import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('tips')
sns.histplot(data=data, x='day', hue = 'sex', kde= True,palette= "spring")
plt.show()