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
cursor.execute('DROP TABLE IF EXISTS ROADPANDA;')
    
cursor.execute('''CREATE TABLE ROADPANDA
       (ID INT NOT NULL,
        PROVIDER_ID INT NOT NULL,
        PROVIDER  CHAR(10),
        LOCATION  CHAR(50),
        SUBLOCATION  CHAR(50),
        BIKE_NAME   CHAR(50),
        AVAILABILITY CHAR (10));''')
print "Table created successfully"

count = 1

'''
def dateNavigation():

    ######START_Date_Time
    count = 0
    while(count<5):
        td0 = time.strftime("%d-%m-%Y")
        print td0
        current_time = datetime.now()
        tt0= current_time + timedelta(hours=1)
        print ("%s:00" %(tt0.hour))

    ######END_Date_Time

        td1 = td0 + datetime.timedelta(days=count)
        print td1
        #tt1 = 
        #print ("%s:00" %(tt0.hour))
        count = count + 1
'''    

def dateNavigation(url):
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
        pageNavigation(tr1,tr2,td,td2,timeVal1,timeVal2,url)
        dateVar=dateVar+timedelta(days=1)

        
def get_week_of_month(year, month, day):
    calendar.setfirstweekday(6)
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] + 1
    return(week_of_month)    
        

   

def pageNavigation(tr,tr2,td,td2,timeVal1,timeVal2, url):

       
            browser1.get(url)
            #browser1.maximize_window()

   
            startTime=browser1.find_element_by_xpath(".//*[@id='start_time']").click()
            pickElementDate = browser1.find_element_by_xpath("html/body/div[1]/div[3]/table/tbody/tr["+str(tr)+"]/td["+str(td)+"]").click()
            pickElementTime = browser1.find_element_by_xpath("html/body/div[1]/div[2]/table/tbody/tr/td/span["+str(timeVal1)+"]").click()
   

    

            endTime=browser1.find_element_by_xpath(".//*[@id='end_time']").click()
            pickElementDate = browser1.find_element_by_xpath("html/body/div[2]/div[3]/table/tbody/tr["+str(tr2)+"]/td["+str(td2)+"]").click()
            pickElementTime = browser1.find_element_by_xpath("html/body/div[2]/div[2]/table/tbody/tr/td/span["+str(timeVal2)+"]").click()
    



            searchButton = browser1.find_element_by_xpath(".//*[@id='rent-form']/div[3]/input").click()
            
            page_info()
            
            
        
       
def page_info():
    ps=browser1.page_source
    soup=BeautifulSoup(ps,"html.parser")
    bikeImageHtml=soup.find_all("img",{"class":"img-responsive"})
    for value in bikeImageHtml:
        pass
        #print(value.get("src"))
    
    count = 1
    for a in soup.find_all("div",{"class":"panel-body"}):                           ###Bike_available
        for b in a.find_all("div",{"class":"name"}):                                 ###Bike_name
            for c in a.find_all("div",{"class":"avl-lbl avl"}):                      ###Bike_available
                for d in a.find_all("span",{"class":"b-name"}):                      ###Bike_location
                    for e in a.find_all("div",{"class":"row price-list"}):           ###Total_tariff
                        for z in soup.find_all("ul",{"id":"helpline"}): 
                            print("Roadpanda")
                            
                            location = " ".join(z.text.split())
                            print(location)
                            print(d.text)
                            bike = " ".join(b.text.split())
                            print(bike)
                            print(c.text)
                            print("************************************")


                            Provider_id=1
                            Provider="RoadPanda"

                            cursor.execute("INSERT INTO  ROADPANDA(ID,PROVIDER_ID,PROVIDER,LOCATION,SUBLOCATION,BIKE_NAME,AVAILABILITY)\
                            VALUES (?,?,?,?,?,?,?)",(count,Provider_id,Provider,location,d.text,bike,c.text))
                            count = count+1
    

    
Location1 = "http://www.roadpanda.com/cities/bangalore"
dateNavigation(Location1)
Location2 = "http://www.roadpanda.com/cities/hyderabad"
dateNavigation(Location2)
Location3 = "http://www.roadpanda.com/cities/mumbai"
dateNavigation(Location3)

print "Records created successfully";
cursor.execute('''SELECT * FROM ROADPANDA''')
print"Select"
                            


for row in cursor:
        print "ID = ", row[0]
        print "PROVIDER_ID = ", row[0]
        print "PROVIDER = ", row[1]
        print "LOCATION = ", row[2]
        print "SUBLOCATION = ", row[3]
        print "BIKE_NAME = ", row[4]
        print "AVAILABILITY = ", row[5]

#provider,location,sublocation,bikeName,available,pID,bID 

cursor.close()   
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






    



