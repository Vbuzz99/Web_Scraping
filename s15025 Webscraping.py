from selenium import webdriver
import webbrowser
from bs4 import BeautifulSoup as soup


#1st page link
url="https://www.walmart.com/browse/cell-phones/appleiphone/1105910_7551331_1127173?povid=GlobalNav_rWeb_Electronics_CellPhones_iPhone&affinityOverride=default&page=1"
edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s' 

#Start automated browser
automated_browser=webdriver.Edge(executable_path=r"G:\VI SEM\IS 3005 - Statistics in Practice I\Guest\msedgedriver.exe") 
webbrowser.get(edge_path).open(url)


#test for the 1st page
#html=automated_browser.page_source
#print(html)
#phone=soup(html,'lxml')
#phone


#Genarate Url
url_list=[ ]
for i in range(1,26):
 url_list.append("https://www.walmart.com/browse/cell-phones/appleiphone/1105910_7551331_1127173?povid=GlobalNav_rWeb_Electronics_CellPhones_iPhone&affinityOverride=default&page=" + str(i))
url_list 


#create lists
item_names=[]
price_list=[]
item_shipping=[]


#obtain data
for url in url_list:
    
    result=automated_browser.get(url)
    
    
    html=automated_browser.page_source
    phone=soup(html,'lxml')
    product_name=phone.findAll('span',{'class':"w_V_DM"})
    product_shipping=phone.findAll('div',{'class':"mt2 mb2"})
    product_price=phone.findAll('div',{'data-automation-id':"product-price"})
    
    for names,shipping,price in zip(product_name,product_shipping,product_price):
        item_names.append(names.span.text.strip())
        item_shipping.append(shipping.span.text.strip())
        price_list.append(price.div.text.strip())

#create an excel file
import pandas as pd
df=pd.DataFrame({'product_Name':item_names,'Price':price_list,'Pickup/Checking':item_shipping})
filepath=r"G:\VI SEM\IS 3005 - Statistics in Practice I\Guest\s15025_CDVP_Basnayake_walmart.xlsx"
df.to_excel(filepath)


