"""
Name: Erick Yoakum
SL: Chase Hult

ISTA 131
Final Project

This program creates a plot comparing the percentages of infants who get the polio vaccine in Britain, France, and Ireland
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def get_ols_parameters(s):
    '''
    Gets statistical parameters from a series

    parameters: s, a series
    returns: List
    '''
    x = s.index.values
    X = sm.add_constant(x)
    model = sm.OLS(s,X)
    results = model.fit()
    return [results.params.loc['x1'], results.params.loc['const'], results.rsquared, results.pvalues['x1']]

def make_linReg(df, cName):
    '''
    Plots a linear regression line

    parameters: df, a dataframe
                cName, a string
    returns: None
    '''
    x = np.arange(2000,2022)
    params = get_ols_parameters(df.loc[cName])
    y = params[0] * x + params[1]
    plt.plot(x,y,linestyle = '--')

def main():
    '''
    Generates a scatter plot with linear regression lines
    '''
    

    #Makes the dataframe
    df =  pd.read_csv('Pol3.csv', index_col= 0)
    df.columns = [2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]
    df = df[df.columns[::-1]]
    x = np.arange(2000,2022)

    #Formating for the plot
    plt.style.use('Solarize_Light2')
    plt.figure(figsize = (12,8))

    #Plots UK data
    plt.scatter(x, df.loc["United Kingdom of Great Britain and Northern Ireland"],s=34)
    make_linReg(df, "United Kingdom of Great Britain and Northern Ireland")

    #Plots French data
    plt.scatter(x, df.loc["France"],s=34)
    make_linReg(df, "France")

    #Plots Ireland data
    plt.scatter(x, df.loc["Ireland"],s=34)
    make_linReg(df, "Ireland")

    #Formating for the plot
    plt.xticks(np.array([2000,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020,2022]))
    plt.title("Percentage of 1-Year-Olds Who Have Received \n Three Doses of Polio Vaccine from 2000-2021 Across Britain, France, & Ireland",fontsize=19)
    plt.xlabel("Years (2000-2021)",fontsize=20)
    plt.ylabel("Percentage of Vaccinated 1 Year Olds", fontsize=20)
    plt.legend(["Great Britain and Northern Ireland","Great Britain and Northern Ireland Regression","France","France Regression","Ireland","Ireland Regression"])
    plt.show()
    

if __name__ == '__main__':
    main()