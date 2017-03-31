from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import codecs
import sqlite3
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import calendar
import numpy as np
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


browser1=webdriver.Chrome()
conn = sqlite3.connect('Database.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS BYKEMANIA;')
    
cursor.execute('''CREATE TABLE BYKEMANIA
       (ID INT NOT NULL,
        PROVIDER_ID INT NOT NULL,
        PROVIDER  CHAR(10),
        LOCATION  CHAR(50),
        SUBLOCATION  CHAR(50),
        BIKE_NAME   CHAR(50),
        AVAILABILITY CHAR (10));''')
print "Table created successfully"
def dateNavigation():
    dateVar=datetime.now()+timedelta(days=1)
    td=0
    tr=0
    td=0
    td2=0
    timeVal1=0
    timeVal2=0
    for x in range(1,2):
        if(dateVar.weekday()<6):
            td=dateVar.weekday()+2
        if(dateVar.weekday()==6):
            td=1
        
        tr1=get_week_of_month(2017, dateVar.month,dateVar.day)    
        timeVal1=randint(1,12)
        timeVal2=randint(1,12)
        
        if(dateVar.weekday()==5):
            td2=1            
        else:
            td2=td+1
        tr2=get_week_of_month(2017, (dateVar+timedelta(days=1)).month,(dateVar+timedelta(days=1)).day)    


        #print("tr=%d tr2=%d td=%d td2=%d timeVal1=%d timeVal2=%d"%(tr1,tr2,td,td2,timeVal1,timeVal2))        
        pageNavigation(tr1,tr2,td,td2,timeVal1,timeVal2)
        dateVar=dateVar+timedelta(days=1)
        
        
    

def pageNavigation(tr,tr2,td,td2,timeVal1,timeVal2):

    array=[1000,1001,1002,1003,1004]
   
    browser1.get("https://www.bykemania.com/")
    
    #time.sleep(4)
    #browser1.maximize_window()
    clickLocation = browser1.find_element_by_xpath(".//*[@id='location']").click()
    i=0
    while i< len(array):

        #print("$$$$$$$$$$$$$$$$$$$$$$$$")
        #print array[i]
        #print("$$$$$$$$$$$$$$$$$$$$$$$$")
       
        pickLocation = browser1.find_element_by_xpath("//*[@value="+str(array[i])+"]").click()
        
    

        clickDateandTime=browser1.find_element_by_xpath("html/body/div[4]/div[1]/div/div[2]/div/form/div[1]/div/input").click()
        enterDateandTime=browser1.find_element_by_xpath("html/body/div[4]/div[1]/div/div[2]/div/form/div[1]/div/input").send_keys('2017/04/1 15')
   
        clickDateandTime=browser1.find_element_by_xpath("html/body/div[4]/div[1]/div/div[2]/div/form/div[2]/div/input").click()
        enterDateandTime=browser1.find_element_by_xpath("html/body/div[4]/div[1]/div/div[2]/div/form/div[2]/div/input").send_keys('2017/04/2 17')



        searchButton =   browser1.find_element_by_xpath("//*[@value='Go']").click()

        if(array[i]==1000):
            Location = "Koramangala(opp. Forum Mall)"
        elif(array[i]==1001):
            Location = "Kumaraswamy layout(near Dayananda Sagar College)"
        elif(array[i]==1004):
            Location = "Mathikere (Near Ramaiah college)"
        elif(array[i]==1003):
            Location = "V.V. Puram(near Lalbagh)"
        elif(array[i]==1002):
            Location = "Kumaraswamy layout(near HDFC Bank Atm)"
        
        page_info(Location)
        
        i+=1
        home = browser1.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-2']/a[1]/span").click()
       


    
def get_week_of_month(year, month, day):
    calendar.setfirstweekday(6)
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] + 1
    return(week_of_month)


def page_info(Location):
    ps=browser1.page_source
    soup=BeautifulSoup(ps,"html.parser")
    bikeImageHtml=soup.find_all("img",{"height":"130px"})           ###Bike_image
    for value in bikeImageHtml:
        pass
        #print(value.get("src"))
    count = 1
    for a in soup.find_all("div",{"class":"thumbnail col-lg-10 col-md-10 col-sm-10"}):
        for b in a.find_all("span",{"style":"font-size: 15px; font-weight: bold;"}):  ###Bike_name
            for c in a.find_all("span",{"style":"color:green"}):                ###Bike_availability
                for d in a.find_all("div",{"style":"padding-bottom: 8px"}):     ###Bike_location
                    #print ("Bykemania")
                    print b.text
                    print c.text
                    print d.text
                    print("****************************************")
                    
                    Provider_id=4
                    Provider="Bykemania"
                    Availability = "Available"
                    MainLocation = "Bangalore"

                    cursor.execute("INSERT INTO  BYKEMANIA(ID,PROVIDER_ID,PROVIDER,LOCATION,SUBLOCATION,BIKE_NAME,AVAILABILITY)\
                    VALUES (?,?,?,?,?,?,?)",(count,Provider_id,Provider,MainLocation,Location,b.text,Availability))
                    count = count+1


    

'''    
    l=[]
    d={}
    for value in bike_title:       
        a=" ".join(value.text.split())
        k,v=a.split("Total Fare")
        d[k]=v.split(':')
        l.append(d)
       
    print(l)
    print(len(l))
   # print(len(myDict))

        

    bikeTitleList=[]
    bikeImgSrcList=[]
    for value in bikeTitleUL:
        tempList=[]
        #print(value)
        for value2 in value.contents[0].contents:
            tempList.append(value2)
        #print(tempList[0].text,tempList[1].contents[0].get("src"))
        bikeTitleList.append(tempList[0].text.encode('utf8'))
        bikeImgSrcList.append(tempList[1].contents[0].get("src").encode('utf8'))
        bikeHourPriceList=soup.find_all("div",{"class":"price effective-price"})
        bikeTotalPriceList=soup.find_all("div",{"class":"price total-price"})
    
        #bikeSoldOut=soup.find_all("div",{"class":"sold-out-wrapper show"})

    for x in range(0,len(bikeTitleList)-1):
        
        print(bikeTitleList[x],bikeImgSrcList[x],bikeHourPriceList[x].text.encode('utf8'),bikeTotalPriceList[x].text.encode('utf8'))
        print("\n \n")

'''

dateNavigation()
cursor.execute('''SELECT * FROM BYKEMANIA''')
#print"Select"
                                                    


for row in cursor:
    print "ID = ", row[0]
    print "PROVIDER_ID = ", row[1]
    print "PROVIDER = ", row[2]
    print "LOCATION = ", row[3]
    print "SUBLOCATION = ", row[4]
    print "BIKE_NAME = ", row[5]
    print "AVAILABILITY = ", row[6]
    


    
'''
ps=browser1.page_source
soup=BeautifulSoup(ps,"html.parser")
bikeImageList=soup.find_all("a",{"class":"media-link"})
'''





