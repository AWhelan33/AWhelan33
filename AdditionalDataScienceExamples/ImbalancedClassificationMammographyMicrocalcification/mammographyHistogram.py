#Create histograms of numeric input variables
from pandas import read_csv
from matplotlib import pyplot
#define the dataset location
filename = 'mammography.csv'
#load the csv file as a data frame
df = read_csv(filename, header=None)
# Histograms of all variables
df.hist()
pyplot.show()