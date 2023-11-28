import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm



DTP3 = pd.read_csv('DTP3.csv', index_col= 0)
HepB3 = pd.read_csv('HepB3.csv', index_col= 0)
Hib3 = pd.read_csv('Hib3.csv', index_col= 0)
MCV1 = pd.read_csv('MCV1.csv', index_col= 0)
MCV2 = pd.read_csv('MCV2.csv', index_col= 0)
Pol3 = pd.read_csv('Pol3.csv', index_col= 0)


df = pd.DataFrame('',['DTP3','HepB3','Hib3','MCV1','MCV2','Pol3'],DTP3.columns)


df.loc['DTP3'] = DTP3.loc["United States of America"]
df.loc['HepB3'] = HepB3.loc["United States of America"]
df.loc['Hib3'] = Hib3.loc["United States of America"]
df.loc['MCV1'] = MCV1.loc["United States of America"]
df.loc['MCV2'] = MCV2.loc["United States of America"]
df.loc['Pol3'] = Pol3.loc["United States of America"]


df.columns = [2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]
df = df[df.columns[::-1]]

plt.plot(df.loc['DTP3'])
#plt.plot(df.loc['HepB3'])
plt.plot(df.loc['Hib3'])
#plt.plot(df.loc['MCV1'])
plt.plot(df.loc['MCV2'])
plt.plot(df.loc['Pol3'])
#plt.xticks(np.array([2000,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020,2022]))
plt.legend(['DTP3','HepB3','Hib3','MCV1','MCV2','Pol3'])


plt.show()