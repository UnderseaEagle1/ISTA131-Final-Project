"""
Name: Erick Yoakum
SL: Chase Hult

ISTA 131
Final Project

This program creates a plot comparing the average percentage of vaccinated infants from 193 countries for 6 diffrent vaccines
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


def main():
    '''
    Generates a percent vs years plot for 6 vaccines
    '''
    
    DTP3 = pd.read_csv('DTP3.csv', index_col= 0)
    DTP3.loc['mean'] = DTP3.mean(axis = 0)

    HepB3 = pd.read_csv('HepB3.csv', index_col= 0)
    HepB3.loc['mean'] = HepB3.mean(axis = 0)

    Hib3 = pd.read_csv('Hib3.csv', index_col= 0)
    Hib3.loc['mean'] = Hib3.mean(axis = 0)

    MCV1 = pd.read_csv('MCV1.csv', index_col= 0)
    MCV1.loc['mean'] = MCV1.mean(axis = 0)

    MCV2 = pd.read_csv('MCV2.csv', index_col= 0)
    MCV2.loc['mean'] = MCV2.mean(axis = 0)

    Pol3 = pd.read_csv('Pol3.csv', index_col= 0)
    Pol3.loc['mean'] = Pol3.mean(axis = 0)



    df = pd.DataFrame('',['DTP3','HepB3','Hib3','MCV1','MCV2','Pol3'],DTP3.columns)


    df.loc['DTP3-Mean'] = DTP3.loc["mean"]
    df.loc['HepB3-Mean'] = HepB3.loc["mean"]
    df.loc['Hib3-Mean'] = Hib3.loc["mean"]
    df.loc['MCV1-Mean'] = MCV1.loc["mean"]
    df.loc['MCV2-Mean'] = MCV2.loc["mean"]
    df.loc['Pol3-Mean'] = Pol3.loc["mean"]


    df.columns = [2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]
    df = df[df.columns[::-1]]
    plt.style.use('Solarize_Light2')
    plt.figure(figsize = (12,8))

    plt.plot(df.loc['DTP3-Mean'])
    plt.plot(df.loc['HepB3-Mean'])
    plt.plot(df.loc['Hib3-Mean'])
    plt.plot(df.loc['MCV1-Mean'])
    plt.plot(df.loc['MCV2-Mean'])
    plt.plot(df.loc['Pol3-Mean'])

    plt.xticks(np.array([2000,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020,2022]))
    plt.legend(['DTP3','HepB3','Hib3','MCV1','MCV2','Pol3'])
    plt.title("Average Percentage of Vaccinated 1-Year-Olds from 2000-2021 Globally", fontsize=19)
    plt.xlabel("Years (2000-2021)",fontsize=20)
    plt.ylabel("Mean Percentage of Vaccinated \n 1-Year-Olds", fontsize=20)


    plt.show()


if __name__ == '__main__':
    main()