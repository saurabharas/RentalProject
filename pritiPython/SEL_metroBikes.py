from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import codecs
import time
import sqlite3
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
cursor.execute('DROP TABLE IF EXISTS METROBIKES;')
    
cursor.execute('''CREATE TABLE METROBIKES
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

    array=[1,2,3,4,5,6,7,15,16,17,18]
    browser1.get("http://metrobikes.in/")
    
    #time.sleep(4)
    #browser1.maximize_window()
    clickLocation = browser1.find_element_by_xpath(".//*[@id='nav']/div[3]/div/div/div[1]/form/label/select").click()

    i=0
    while i< len(array):

        #print("$$$$$$$$$$$$$$$$$$$$$$$$")
        #print array[i]
        #print("$$$$$$$$$$$$$$$$$$$$$$$$")
        
        selectLocation = browser1.find_element_by_xpath(".//*[@value="+str(array[i])+"]").click()
        
        click = browser1.find_element_by_xpath(".//*[@id='nav']/div[3]/div/div/div[2]/a/h1").click()
        time.sleep(5)
        startTime=browser1.find_element_by_xpath(".//*[@id='fromdatepicker']").click()
        time.sleep(5)
        pickElementDate = browser1.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/table/tbody/tr["+str(tr)+"]/td["+str(td)+"]/div").click()
        time.sleep(5)
        pickElementTime = browser1.find_element_by_xpath("html/body/div[4]/div[2]/div/div[1]/div[2]").click()
           

    

    
        time.sleep(5)
        #pickElementDate = browser1.find_element_by_xpath("html/body/div[5]/div[1]/div[2]/table/tbody/tr["+str(tr2)+"]/td["+str(td2)+"]/div").click()
        pickElementDate = browser1.find_element_by_xpath("html/body/div[5]/div[1]/div[2]/table/tbody/tr[5]/td[7]/div").click()
        time.sleep(5)
        pickElementTime = browser1.find_element_by_xpath("html/body/div[6]/div[2]/div/div[1]/div[4]").click()
       




        searchButton =   browser1.find_element_by_xpath(".//*[@id='booking-step1-continue']/a").click()

        only_available = browser1.find_element_by_xpath(".//*[@id='showAvailable']").click()

        if(array[i]==1):
            Location = "Bangalore"
        elif(array[i]==2):
            Location = "Mysore"
        elif(array[i]==3):
            Location = "Jaipur"
        elif(array[i]==4):
            Location = "Udaipur"
        elif(array[i]==5):
            Location = "Belagavi"
        elif(array[i]==6):
            Location = "Manipal"
        elif(array[i]==7):
            Location = "Jaisalmer"
        elif(array[i]==15):
            Location = "Gokarna"
        elif(array[i]==16):
            Location = "Hospet"
        elif(array[i]==17):
            Location = "Chikamagalur"
        elif(array[i]==18):
            Location = "Tumkur"

        page_info(Location)
        i=i+1

        home = browser1.find_element_by_xpath(".//*[@id='step1-li']/a/div").click()

    

       


    
def get_week_of_month(year, month, day):
    calendar.setfirstweekday(6)
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] + 1
    return(week_of_month)


def page_info(Location):
    ps=browser1.page_source
    soup=BeautifulSoup(ps,"html.parser")

    bikeImageHtml=soup.find_all("img",{"class":""})           ###Bike_image
    for value in bikeImageHtml:
        pass
        #print(value.get("src"))
    
    count = 1
    for a in soup.find_all("ul",{"class":"book_bike_fleet happy_customers item"}):  ###Bike_available
        for b in a.find_all("h6",{"class":""}):                                     ###Bike_name
            for c in a.find_all("optgroup",{"label":"Available at"}):               ###Bike_location
                for d in a.find_all("div",{"class":"price effective-price"}):       ###Hourly_rate
                    for e in a.find_all("div",{"class":"price total-price"}):       ###Total_tariff
                        #print(b.text)
                        #print(c.text)
                        #print(d.text)
                        #print(e.text)
                        #print("************************************")

                        Provider_id=2
                        Provider="MetroBikes"
                        Availability = "Available"

                        cursor.execute("INSERT INTO  METROBIKES(ID,PROVIDER_ID,PROVIDER,LOCATION,SUBLOCATION,BIKE_NAME,AVAILABILITY)\
                        VALUES (?,?,?,?,?,?,?)",(count,Provider_id,Provider,Location,c.text,b.text,Availability))
                        count = count+1

    
                        
                
#provider,location,sublocation,bikeName,available,pID,bID           




#cursor.close()       
        

    
    
'''    l=[]
    d={}
    for value in bike_title:       
        a=" ".join(value.text.split())
        k,v=a.split("Total Fare")
        d[k]=v.split(':')
        l.append(d)
       
    print(l)
    print(len(l))
   # print(len(myDict))

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

                     
dateNavigation()

#print "Records created successfully";
cursor.execute('''SELECT * FROM METROBIKES''')
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


'''
1.find weekday
2.for (!sunday)
    td=weekday+2
    tr=get_week_of_the_month(currentDate)
    findelementbyxpath(td,tr).click
if(sunday):
    td=0

    
'''
