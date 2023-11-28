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

def make_linReg(df, cName):
    x = np.arange(2000,2022)
    params = get_ols_parameters(df.loc[cName])
    y = params[0] * x + params[1]
    plt.plot(x,y,linestyle = '--')

def main():
    #plt.style.use('fivethirtyeight')
    plt.style.use('Solarize_Light2')

    
    df =  pd.read_csv('Pol3.csv', index_col= 0)
    df.columns = [2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]
    df = df[df.columns[::-1]]
    x = np.arange(2000,2022)


    plt.figure(figsize = (12,8))

    plt.scatter(x, df.loc["United Kingdom of Great Britain and Northern Ireland"],s=34)
    make_linReg(df, "United Kingdom of Great Britain and Northern Ireland")


    plt.scatter(x, df.loc["France"],s=34)
    make_linReg(df, "France")

    plt.scatter(x, df.loc["Ireland"],s=34)
    make_linReg(df, "Ireland")


    plt.xticks(np.array([2000,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020,2022]))
    
    #plt.yticks(np.array([0,10,20,30,40,50,60,70,80,90,100]))
    #plt.yticks(np.arange(90,100))
    plt.title("Percentage of 1-Year-Olds Who Have Received \n Three Doses of Polio Vaccine from 2000-2021 Across Britain, France, & Ireland",fontsize=19)
    plt.xlabel("Years (2000-2021)",fontsize=20)
    plt.ylabel("Percentage of Vaccinated 1 Year Olds", fontsize=20)
    plt.legend(["Great Britain and Northern Ireland","Great Britain and Northern Ireland Regression","France","France Regression","Ireland","Ireland Regression"])
    plt.show()
    

if __name__ == '__main__':
    main()