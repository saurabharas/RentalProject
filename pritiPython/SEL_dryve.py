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
import re


browser1=webdriver.Chrome()
conn = sqlite3.connect('Database.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS DRYVE;')
    
cursor.execute('''CREATE TABLE DRYVE
       (ID INT NOT NULL,
        PROVIDER_ID INT NOT NULL,
        PROVIDER  CHAR(10),
        LOCATION  CHAR(50),
        SUBLOCATION  CHAR(50),
        BIKE_NAME   CHAR(50),
        AVAILABILITY CHAR (10));''')
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

    array=['HSR Layout','Mahadevpura','Koramangala','RT Nagar','Horamavu/Banaswadi']
    i=0
    browser1.get("https://dryve.co.in/home")
    #browser1.maximize_window()
    
    dateOuter = browser1.find_element_by_xpath(".//*[@id='dropdownStart']/div/input").click()
    pickElementDate = browser1.find_element_by_xpath(".//*[@id='top']/search-bar/section/form/div/div/div[1]/ul/div/table/tbody/tr["+str(tr)+"]/td["+str(td)+"]").click()
    pickElementTime = browser1.find_element_by_xpath(".//*[@id='top']/search-bar/section/form/div/div/div[1]/ul/div/table/tbody/tr/td/span["+str(timeVal1)+"]").click()

    dateOuter = browser1.find_element_by_xpath(".//*[@id='dropdownEnd']/div/input").click()
    pickElementDate = browser1.find_element_by_xpath(".//*[@id='top']/search-bar/section/form/div/div/div[2]/ul/div/table/tbody/tr["+str(tr2)+"]/td["+str(td2)+"]").click()
    pickElementTime = browser1.find_element_by_xpath(".//*[@id='top']/search-bar/section/form/div/div/div[2]/ul/div/table/tbody/tr/td/span["+str(timeVal2)+"]").click()

    #print("$$$$$$$$$$$$$$$$$$$$$$$$")
    #print array[i]
    #print("$$$$$$$$$$$$$$$$$$$$$$$$")
    location =   browser1.find_element_by_xpath(".//*[@id='location']").click()
    pickLocation = browser1.find_element_by_xpath("//*[@label="+"\'"+array[i]+"\'"+"]").click()
    searchButton =   browser1.find_element_by_xpath(".//*[@id='top']/search-bar/section/form/div/div/div[5]/a").click()
    page_info()
    i=i+1
    
    while i< len(array):

        

        #print("$$$$$$$$$$$$$$$$$$$$$$$$")
        #print array[i]
        #print("$$$$$$$$$$$$$$$$$$$$$$$$")
        location =   browser1.find_element_by_xpath(".//*[@id='location']").click()
        pickLocation = browser1.find_element_by_xpath("//*[@label="+"\'"+array[i]+"\'"+"]").click()
        

        page_info()
        
        i+=1
        
    
def get_week_of_month(year, month, day):
    calendar.setfirstweekday(6)
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] + 1
    return(week_of_month)


def page_info():
    time.sleep(10)
    ps=browser1.page_source
    #time.sleep(10)
    soup=BeautifulSoup(ps,"html.parser")
   #print "((((((((((()))))))))))))))))"

    count = 1
    for a in soup.find_all("div",{"class":"bikes_list_outer ng-scope"}):                           ###Bike_available
        for b in a.find_all("h4",{"class":"ng-binding"}):                                 ###Bike_name
            for c in a.find_all("select",{"class":"location-name ng-pristine ng-untouched ng-valid ng-not-empty"}):                      ###Bike_availablefor d in a.find_all("span",{"class":"ng-binding"}):                      ###Bike_location
                    for d in a.find_all("a",{"ng-class":"{grayOut: locdata.availability==false}"}):           ###Total_tariff
                        
                            #print("Dryve")
                            
                            #print(b.text)
                            #print(c.text)
                
                            #print(d.text)
                            
                            #print("************************************")
                            Provider_id=3
                            Provider="Dryve"
                            Availability = "Available"
                            Location = "Bangalore"

                            cursor.execute("INSERT INTO DRYVE(ID,PROVIDER_ID,PROVIDER,LOCATION,SUBLOCATION,BIKE_NAME,AVAILABILITY)\
                            VALUES (?,?,?,?,?,?,?)",(count,Provider_id,Provider,Location,c.text,b.text,Availability))
                            count = count+1



'''    print(len(bike_title))
    l=[]
    d={}
    for value in bike_title:
        a=" ".join(value.text)
        a= value.text.replace("\n",' ')
        final= a.encode("ascii","ignore")
        k,v=final.split('Total')
        d[k]=v.split(':')
        
        l.append(d)
        print l
        #print(re.findall('%d',l))
'''        
dateNavigation()


cursor.execute('SELECT * FROM DRYVE;')
for row in cursor:
    print "ID = ", row[0]
    print "PROVIDER_ID = ", row[1]
    print "PROVIDER = ", row[2]
    print "LOCATION = ", row[3]
    print "SUBLOCATION = ", row[4]
    print "BIKE_NAME = ", row[5]
    print "AVAILABILITY = ", row[6]


'''
print"Select WITH CONDITION###################"
cursor.execute(' SELECT * FROM DRYVE WHERE ID = 8;')
print cursor.fetchall()
'''           
   

'''    bikeTitleList=[]
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




    
'''
ps=browser1.page_source
soup=BeautifulSoup(ps,"html.parser")
bikeImageList=soup.find_all("a",{"class":"media-link"})
'''



