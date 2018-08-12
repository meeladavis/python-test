# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reset default params
sns.set()
dtype1 = {
    'names':
        ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    'formats':
        ('f8', 'f8', 'f8', 'f8', '|S15')
        }
filename = '/Users/meeladavis/Python/pythonscripts/viz/iris.data'
#irisdata =  np.loadtxt(filename,
#            dtype=dtype1,
#            delimiter=',', skiprows=1)

irisdata =  pd.read_csv(filename,sep=',',skiprows=1, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'], converters={'sepal_length':np.float32}, dtype = {'sepal_length': np.float32, 'sepal_width': np.float32, 'petal_length': np.float32, 'petal_width': np.float32, 'species': np.str})

# Load iris data
iris = sns.load_dataset('irisdata')
sns.violinplot(y=["sepal_length"] )

plt.show()

# Construct iris plot
#sns.swarmplot('irisdata')

# Show plot
#plt.show()
