# library & dataset
print('hi')
import numpy as np
print('numpy')
import seaborn as sns
print('seaborn')

print('hi2')

filename = '/Users/meeladavis/Python/pythonscripts/Viz/iris.csv'
print(filename)

#iris =  np.genfromtxt(filename, delimiter=',', dtype=None)
#iris =  np.loadtxt(filename, delimiter=',', dtype=None)


iris =  np.loadtxt(filename,
            dtype={
            'names': ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
            'formats': (np.float, np.float, np.float, np.float, '|S15')},
            delimiter=',', skiprows=0)
          #usecols=[0,1,2,3,4],

print('iris')

df = sns.load_dataset('iris')
print('hi3')
# Just switch x and y
prinf(str(df))
sns.violinplot( y=df["species"], x=df["sepal_length"] )

sns.violinplot(df)
sns.plt.show()
