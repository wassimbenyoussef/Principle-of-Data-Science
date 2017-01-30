# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:45:17 2016

@author: wassim
"""


import csv as csv
import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
from matplotlib import dates
from collections import Counter
import datetime

attacks = pd.read_csv('attacks.csv', encoding = 'ISO-8859-1', sep = ',', error_bad_lines=False)
print(attacks.head(10))

# See the number of attacks
attacks.shape

#See the number of missing values
print (attacks.shape[0] - attacks.count())

#Visualisation of the data

country_count = attacks['Country'].value_counts()
print(country_count)
nb_values = pd.Series.unique(attacks['Country'])
#Number of different countries
len(nb_values)
country_count2 = Counter(attacks['Country'].dropna().tolist()).most_common(30)
country_count_index = [table[0] for table in country_count2]
country_count_values = [table[1] for table in country_count2]
fig,ax = plt.subplots(figsize=(10,8))
sbn.barplot(x = country_count_values, y = country_count_index, ax=ax, orient='h')
plt.title('Total 30 most common countries')
plt.xlabel('number of attacks')
plt.ylabel('Country')

#Evolution of number of attacks over time


date2 = np.arange(attacks.shape[0])
print(attacks['Date'][5])
for i in range(2 , attacks.shape[0]):
    date_test = datetime.datetime.strptime(attacks['Date'][i], '%d-%b-%Y')
    date2[i] = dates.date2num(date_test)




type_count = attacks['Type'].value_counts()
print(type_count)
type_index = type_count.index
type_values = type_count.values

fig,ax = plt.subplots(figsize=(8,6))
sbn.barplot(x = type_values , y = type_index , ax =ax )
plt.title('Total type')
plt.xlabel('Counter')
plt.ylabel('Type')



    
    








    