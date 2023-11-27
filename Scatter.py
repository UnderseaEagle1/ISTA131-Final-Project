import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def get_ols_parameters(s):
    '''
    gets statistical parameters from a series

    parameters: s, a series
    returns: List
    '''
    x = s.index.values
    X = sm.add_constant(x)
    model = sm.OLS(s,X)
    results = model.fit()
    return [results.params.loc['x1'], results.params.loc['const'], results.rsquared, results.pvalues['x1']]

def make_linReg_scatter(df, cName):
    x = np.arange(2000,2022)
    plt.scatter(x ,df.loc[cName])
    params = get_ols_parameters(df.loc[cName])
    y = params[0] * x + params[1]
    plt.plot(x,y)

def main():
    df =  pd.read_csv('Pol3.csv', index_col= 0)
    df.columns = [2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]
    df = df[df.columns[::-1]]

    
    make_linReg_scatter(df, "Afghanistan")


    plt.xticks(np.array([2000,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020,2022]))
    plt.yticks(np.array([0,10,20,30,40,50,60,70,80,90,100]))

    plt.title("")
    plt.xlabel("Years")
    plt.ylabel("Percentage of 1-year-olds Who Have Received Three Doses of Polio Vaccine")
    plt.legend(["Afghanistan"])

    plt.show()

if __name__ == '__main__':
    main()