"""

author SubashPalvel


"""


# import statements 
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import csv   
import pandas as pd


# initialize a dataframe
data=[]
df=pd.DataFrame(data,columns=['Company Name','Country','Product'])

# code for getting details from a website
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.volza.com/buyers-united-states/united-states-importers-buyers-of-rice?yes=brilliant')
content = driver.page_source
soup = BeautifulSoup(content,'lxml')
print('--------------------------------Getting Details----------------------------------------')
companies=soup.find_all('div',class_="buyers-box pd-5 vertical-top pb-3 pl-3")
count=0
for company in companies:
    if count<6:
        count+=1
        companyname=company.find('div',class_="buy-head-title global-search-buy-box-heading").text
        cn=f'{companyname.strip()}'
        country=company.find('div',class_="countryName-font-size countryname-border buyers-card-country buy-country global-search-color").text
        con=f'{country.strip()}'
        products=company.find('div',class_='pr-3 b-right-col buyer-card-text buyer-card-value').text
        pn=f'{products.strip()}'
        detail=pd.Series(data=[cn,con,pn],index=df.columns,name=count)
        df=df.append(detail)
        print('-----------------------------')

# to save details in excel file
df.to_excel('final.xlsx')
print(df) 
    
