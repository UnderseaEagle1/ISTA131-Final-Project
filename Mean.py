import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


df =  pd.read_csv('Pol3.csv', index_col= 0)
df.columns = [2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]
df = df[df.columns[::-1]]

df.loc['mean'] = df.mean(axis = 0)
df.loc['median'] = df.median(axis = 0)
#plt.xticks(np.array([2000,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020,2022]))
#plt.hist(df.loc['mean'])
#plt.hist(df.loc['median'])
plt.hist(df[2021], color = 'purple')
plt.title("Percentages of 1-year-olds who have received \n three doses of polio vaccine in 2021 Globally",fontsize=19)
plt.xlabel("Percentage",fontsize=20)
plt.ylabel("Frequency", fontsize=20)
plt.show()