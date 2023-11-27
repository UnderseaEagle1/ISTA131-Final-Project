import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def get_ols_parameters(s):
    '''
    gets statistical parameters from a series

    parameters: S, a series
    returns: List
    '''
    x = s.index.values
    X = sm.add_constant(x)
    model = sm.OLS(s,X)
    results = model.fit()
    return [results.params.loc['x1'], results.params.loc['const'], results.rsquared, results.pvalues['x1']]


df =  pd.read_csv('Pol3.csv', index_col= 0)

df = df[df.columns[::-1]]


#for col in df.index:
#    plt.scatter(np.arange(2000,2022),df.loc[col], s= 5, c = 'gray')
x = np.arange(2000,2022)
y= np.array(df.loc["Afghanistan"].values)
X = sm.add_constant(x)
model = sm.OLS(y, X)
#results = model.fit()

#y1 = results.params.loc['x1'] * x + results.params.loc['const']




plt.scatter(x ,df.loc["Afghanistan"])



#params = get_ols_parameters(df.loc["Afghanistan"])
#y = params[0] * x + params[1]
plt.plot(x,y1)




plt.xticks(np.array([2000,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020,2022]))
plt.yticks(np.array([0,10,20,30,40,50,60,70,80,90,100]))
#plt.legend(["Afghanistan"])


plt.show()