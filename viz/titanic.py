import pandas as pd
# Let's get the more detailed Titanic data set
titanic3 = pd.read_excel('/Users/meeladavis/Python/pythonscripts/viz/titanic3.xls')
titanic3.head()
# We can use a factorplot to count categorical data
import matplotlib.pyplot as plt
import seaborn as sns
# Call sns.set() to change the default styles for matplotlib to use Seaborn styles.
sns.set()

sns.catplot('sex', data=titanic3, kind='count')
plt.show()
# Let's bring class in too:
sns.catplot('pclass', data=titanic3, hue='sex', kind='count')
plt.show()
# Of course we can aggregate the other way too
sns.catplot('sex', data=titanic3, hue='pclass', kind='count')
plt.show()
