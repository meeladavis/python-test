##Visualisation test
#https://python-graph-gallery.com/58-show-number-of-observation-on-violinplot/
#https://www.data-to-viz.com/#violin


# library & dataset
import numpy as np
#import requests

# Load dataset from github
import wget
url = 'https://raw.githubusercontent.com/zonination/perceptions/master/probly.csv'
wfilename = wget.download(url)

#import shutil
#shutil.move("../violin_data.csv", "./violin_data.csv")
filename = 'violin_data.csv'
print(filename)

rawdata =  np.loadtxt(filename, skiprows=1, delimiter=",")


# library & dataset
import seaborn as sns
#df = sns.load_dataset('iris')
df = sns.load_dataset(rawdata)
# Just switch x and y
sns.violinplot( y=df["species"], x=df["sepal_length"] )
sns.plt.show()
