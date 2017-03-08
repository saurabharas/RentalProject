from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import codecs
#from pyvirtualdisplay import Display
#from lxml import html
#from xvfbwrapper import Xvfb
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import calendar
import numpy as np
from random import randint



browser1=webdriver.Chrome()
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


        print("tr=%d tr2=%d td=%d td2=%d timeVal1=%d timeVal2=%d"%(tr1,tr2,td,td2,timeVal1,timeVal2))        
        pageNavigation(tr1,tr2,td,td2,timeVal1,timeVal2)
        dateVar=dateVar+timedelta(days=1)
        
        
    

def pageNavigation(tr,tr2,td,td2,timeVal1,timeVal2):
    browser1.get("https://www.royalbrothers.in/")
  
   # nextButton = browser1.find_element_by_xpath(".//*[@id='redirect_city']/div/div[2]/form/div[3]/button").click()

    selectCityButton = browser1.find_element_by_xpath(".//*[@id='city1']").click()

    ##########     BENGALARU    ###########
    
    selectCity = browser1.find_element_by_xpath("html/body/div[2]/div/div[1]/div/nav/div/div[1]/div/div[3]/div[2]/div[2]/div/div/a[1]").click() 

    pickElementDate = browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[1]/div/input").click()
    pickDate = browser1.find_element_by_xpath("html/body/div[6]/div[3]/table/tbody/tr["+str(tr)+"]/td["+str(td)+"]").click()
    pickElementTime = browser1.find_element_by_xpath(".//*[@id='picktime']").click()
    pickTime = browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[2]/div/div[2]/div[3]").click()



    pickElementDate = browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[3]/div/input").click()
    pickDate = browser1.find_element_by_xpath("html/body/div[7]/div[3]/table/tbody/tr["+str(tr)+"]/td["+str(td)+"]").click()
    pickElementTime = browser1.find_element_by_xpath(".//*[@id='picktime2']").click()
    pickTime = browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[4]/div[2]/div[5]").click()




    pickLocation = browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[5]/div/span/select").click()
    pickLocation1 = browser1.find_element_by_xpath("//*[@value='Airport at Shivas Gateway']").click()


    searchButton =   browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[6]/div/input").click()
    closeButton =  browser1.find_element_by_xpath(".//*[@id='front_message']/div/button").click()
  

    page_info()


def get_week_of_month(year, month, day):
    calendar.setfirstweekday(6)
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] + 1
    return(week_of_month)


def page_info():
    ps=browser1.page_source
    soup=BeautifulSoup(ps,"html.parser")
    bikeImageHtml=soup.find_all("img",{"style":"width:100%;"})
    for value in bikeImageHtml:
        pass
        #print(value.get("src"))

    bike_title=soup.find_all("div",{"class":"item-details"})
    for v in bike_title:
        #pass
        print(v.text)
    #print bike_title
    print(len(bike_title))

    l=[]
    d={}
    for value in bike_title:       
        a=" ".join(value.text)
        a= value.text.replace("\n",' ')
        final= a.encode("ascii","ignore")
        k,v=final.split('Free')
        d[k]=v.split(':')
       
        l.append(d)


    print(l)
    print(len(l))

  
dateNavigation()

'''
    for value in bike_title:       
        a=" ".join(value.text.split())
        final= a.encode("ascii","replace")
        k,v=final.split("Free")
        d[k]=v.split(':')
        l.append(d)
'''

    
       
   
