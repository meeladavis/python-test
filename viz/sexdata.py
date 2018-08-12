import pandas as pd
import numpy as np
#fname = '/Users/meeladavis/Python/pythonscripts/viz/eg6-a-student-data.txt'
#fname = '/Users/meeladavis/Python/pythonscripts/viz/sexdata.txt'
#Sdtype1 = np.dtype([('gender', '|S1'), ('height', 'f8')])
#sexdata = np.loadtxt(fname, dtype=dtype1, skiprows=0, usecols=(1,3))

data = pd.read_csv('/Users/meeladavis/Python/pythonscripts/viz/sexdata.txt', sep=" ", header=None, usecols=(1,3), names = ["gender", "height"])
#data.columns = ["gender", "height"]


import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
df = sns.load_dataset('data')
sns.catplot( y=df['gender'], x=df['height'] )
#sns.violinplot(df)
plt.show()
