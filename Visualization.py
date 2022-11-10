# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:24:30 2022

@author: Adeolu
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def create_dataframe(url):
    """
    

    This reads the document saved in a comma delimeted format
    ----------
    url : The file path of the document.
    
    """
    data = pd.read_csv(url)
    return data



data = create_dataframe(r"C:\Users\Adeolu\OneDrive\Desktop\uh\Applied Data Science 1\fertility NA\crime\Crime.csv")
data1 = create_dataframe(r"C:\Users\Adeolu\OneDrive\Desktop\uh\Applied Data Science 1\fertility NA\crime\GDP.csv")
data2 = create_dataframe(r"C:\Users\Adeolu\OneDrive\Desktop\uh\Applied Data Science 1\fertility NA\crime\Unemployment1.csv")
data3 = create_dataframe(r"C:\Users\Adeolu\OneDrive\Desktop\uh\Applied Data Science 1\fertility NA\Birthrate.csv")
data4 = create_dataframe(r"C:\Users\Adeolu\OneDrive\Desktop\uh\Applied Data Science 1\fertility NA\Population1.csv")
data5 = create_dataframe(r"C:\Users\Adeolu\OneDrive\Desktop\uh\Applied Data Science 1\fertility NA\Death.csv")
data6 = create_dataframe(r"C:\Users\Adeolu\OneDrive\Desktop\uh\Applied Data Science 1\fertility NA\hiv.csv")



#The use of the DatetimeIndex to extract the year attribute from its datea
data['year'] = pd.DatetimeIndex(data['Date']).year
data2['year'] = pd.DatetimeIndex(data2['date']).year
data3['year'] = pd.DatetimeIndex(data3['date']).year
data4['year'] = pd.DatetimeIndex(data4['date']).year



#Adding of column name/label in the data
data2.columns = ['date','Unemployment Rate','year']
data3.columns = ['date','Births per Woman','Annual % Change','year']
data4.columns = ['date','Population','Annual Growth Rate','year']



#Plotting of a scatter graph to explain relationship between data
plt.figure(figsize=(10,5))
plt.scatter(data['year'],data['Rate of crime'],color='red',label='Crime Rate')
plt.scatter(data1['Year'],data1['GDP'],color='green',label='GDP Rate')
plt.scatter(data2['year'],data2['Unemployment Rate'],color='blue',
            label='Unemployment Rate')
plt.title('Guatemala"s rate of crime to its unemployment')
plt.legend()
plt.savefig('Guatemala.png')
plt.show()



#Plotting of a line graph to show the trend
plt.figure()
plt.plot(data4['year'], data4['Annual Growth Rate'], color='red',
            label='Growth Rate', linestyle='solid')
plt.plot(data3['year'], data3['Births per Woman'], color='blue',
           label='Birth Rate',linestyle='dashed')
plt.plot(data5['Year'], data5['Death Rate'], color='green',
           label='Death Rate', linestyle='dotted')
plt.title('North America')
plt.legend()
plt.savefig('NA.png')
plt.show()



#Creating a new column to reduce the bulkiness of its value
data6["CIT"] = data6["Value"]/1000
a = data6.groupby(['Location','Period']).sum().unstack().loc[:,'CIT']

#The indx is used to give a range of its label 
label = ['1990','2001','2011','2021']
indx = np.arange(len(label))
w = 0.2
#Plotting of a stacked bar chart to see the changes that occured,
#at different regions 
#the indx-w/2 represents the location at which the bar starts from
fig, plt = plt.subplots(figsize=(10, 10))
plt.bar(indx-w/2, a.loc['Africa'], label= 'Africa', width=w)
plt.bar(indx+w, a.loc['Americas'], label= 'America', width=w)
plt.bar(indx-w, a.loc['Europe'], label= 'Europe', width=w)
plt.bar(indx+w/4, a.loc['South-East Asia'], label= 'S.E.A', width=w)

#Using the annotate function wher the 
#x_axis: i.get_x() + i.get_width() / 2
# y-axis: i.get_height() which is the label of the bar
#ha is the horizontal alignment and va is vertical alignment
for i in plt.patches:
    plt.annotate(format(i.get_height()),
                   (i.get_x() + i.get_width() / 2,
                    i.get_height()), ha='center', va='center',
                   size=6, xytext=(0, 2), fontweight='bold',
                   textcoords='offset points')


    plt.legend()
    plt.set_xticks(indx)
    plt.set_xticklabels(label)
    plt.set_title('HIV confirmed cases')
    fig.savefig('HIVcases.png')
    




