"""
Name: Erick Yoakum
SL: Chase Hult

ISTA 131
Final Project

This program creates a histogram comparing frequency of the percentages of infants who get the polio vaccine from all 193 countries in the dataset
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


df =  pd.read_csv('Pol3.csv', index_col= 0)
df.columns = [2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]
df = df[df.columns[::-1]]

df.loc['mean'] = df.mean(axis = 0)
df.loc['median'] = df.median(axis = 0)

plt.style.use('Solarize_Light2')
plt.hist(df[2021], color = '#6c71c4')
plt.title("Percentages of 1-year-olds who have received \n three doses of polio vaccine in 2021 Globally",fontsize=19)
plt.xlabel("Percentage of Vaccinated 1-year-olds",fontsize=20)
plt.ylabel("Frequency", fontsize=20)
plt.xticks(np.array([0,10,20,30,40,50,60,70,80,90,100]))
plt.yticks(np.array([0,10,20,30,40,50,60,70,80,90,100]))
plt.show()