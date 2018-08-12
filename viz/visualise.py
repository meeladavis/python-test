##Visualisation test
#https://python-graph-gallery.com/58-show-number-of-observation-on-violinplot/
#https://www.data-to-viz.com/#violin

#datasets - https://github.com/mwaskom/seaborn-data

# library & dataset
import numpy as np
#import requests

# Load dataset from github
#import wget
#url = 'https://raw.githubusercontent.com/zonination/perceptions/master/probly.csv'
#wfilename = wget.download(url)
#print(wfilename)
#import shutil
#shutil.move("../violin_data.csv", "./violin_data.csv")
filename = '/Users/meeladavis/Python/pythonscripts/Viz/iris.csv'
print(filename)

iris =  np.loadtxt(filename, delimiter=",")
print(iris)

# library & dataset
import seaborn as sns
#df = sns.load_dataset('iris')
df = sns.load_dataset("iris")
# Just switch x and y
sns.violinplot( y=df["species"], x=df["sepal_length"])
sns.plt.show()
