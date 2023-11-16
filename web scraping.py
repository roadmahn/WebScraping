# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:18:29 2023

@author: OABI
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

#   open an HTML file on local storage
#with open('googlesearch.html', 'r') as html_file:
#    content = html_file.read()
##    print (content)
#    
#    # printify prints it out as it is in the html file.
#    soup = BeautifulSoup(content, 'lxml')
#    print(soup.prettify())
#    
## how to find specific tags on a html file (h5 is th eHTML tag from the website)
#    tags = soup.find_all('H5')
#    print (tags)
#    
#    open a web page, bu this time we use requests library to do so.
html_text = requests.get('https://disfold.com/united-states/sector/healthcare/companies/').text
#print (html_text)

#using Beautifulsou to extrctt the data like previously used on HTML file
soup =  BeautifulSoup(html_text, 'lxml')
tab = soup.find('table' , class_="striped")
#headr = soup.find('thead')
title = tab.find_all('th')
#print(title)

title_name =  [item.text for item in title]
#print(title_name)

#now create a dataframe using panadas library

df = pd.DataFrame(columns = title_name)
df
# scrolling through the dfferent pages
pages = soup.find('li' , class_="waves-effect")

for page in pages:

#print(datafrm)
# finding each row of data in the table, the rows are tagged with a 'tr'
    column_data = tab.find_all('tr')
    #we now loop through each row to find individual data which is tagged by 'td'
    for row in column_data[1:]:
        row_data = row.find_all('td')
    #    then loop through each individual dtat to clean out the information
        data = [info.text.strip() for info in row_data]
    #trying to eliminate rows without any data
        if len(data) == 1:
            continue
    #    print(data)
    #    print(len(data))
    #    add each row to the dataframe by checking the length of the dataframe.
        length = len(df)
        df.loc[length] = data
    #    print(df)
    #    datafrm = pd.DataFrame(rows = row)
    print(df)
# pushing the dataframe into a csv file and removing the extra column with(index = false)
df.to_csv(r'D:\Scripts\scrape.csv', index = False)