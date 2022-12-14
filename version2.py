"""import required libraries"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def csv(path): 
  """function that reads csv and returns country and year data frame"""
  readData = pd.read_csv(path)
  countries = readData['Country Name'].tolist()
  countries = pd.DataFrame(countries, columns = ['Country'])
  readData.drop('Country Name', inplace=True, axis=1)
  print("COUNTRIES DATA FRAME")
  display(countries)
  print("YEARS DATA FRAME")
  display(readData)
  return countries, readData

def linePlot(name,year):
  """line plot for forest areas of different countries over a decade"""
  l = []
  for i in range(len(year['2001'])):
    d = year.loc[year['2001']==year['2001'][i]].values.flatten().tolist()
    l.append(d)
    d = []
  year = [i for i in year]
  countries = name['Country'].tolist()
  plt.figure(figsize=(20, 8))
  plt.grid()
  for i in range(10):
    plt.plot(year,l[i], lw = 3, ls='dashdot',label=countries[i])
  plt.legend()
  plt.title("FOREST AREAS OF DIFFERENT COUNTRIES OVER A DECADE",size=20)
  plt.xlabel("Year",size=15)
  plt.ylabel("% of Forest area",size=15)
  plt.show()


print("The data is about forest area for different countries over a decade\n\n\n")
countryName, year = csv("/content/forest_area.csv")

print("\n\n")
linePlot(countryName,year)
print('\n\n')

"""Finding the average forest area for different countries"""
averageForestArea = list(year.mean(axis = 1)) # finding the average forest area
countries = countryName['Country'].tolist()
averageDataFrame = pd.DataFrame(list(zip(countries,averageForestArea)),columns=['Country', 'Average foerst area'])
display(averageDataFrame)

"""Correlation of few indicators for the country Australia"""
data = pd.read_csv('/content/Australia.csv')
correlation = data.corr()
plt.title("Correlation between few indicators for Australia \n\n")
display(correlation)

