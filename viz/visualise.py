##Visualisation test
#https://python-graph-gallery.com/58-show-number-of-observation-on-violinplot/
#https://www.data-to-viz.com/#violin

#datasets - https://github.com/mwaskom/seaborn-data

# library & dataset
import numpy as np
#import requests

filename = '/Users/meeladavis/Python/pythonscripts/Viz/iris.csv'

iris =  np.load_txt(filename, delimiter=",")
print(iris)

# library & dataset
import seaborn as sns
#df = sns.load_dataset('iris')
df = sns.load_dataset("iris")
# Just switch x and y
sns.violinplot( y=df["species"], x=df["sepal_length"])
sns.plt.show()
