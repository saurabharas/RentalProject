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



#browser1=webdriver.Chrome()
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.geolocation" :2}
options.add_experimental_option("prefs",prefs)
browser1 = webdriver.Chrome(chrome_options=options)
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


        print("tr=%d tr2=%d td=%d td2=%d timeVal1=%d timeVal2=%d"%(tr1,tr2,td,td2,timeVal1,timeVal2))        
        pageNavigation(tr1,tr2,td,td2,timeVal1,timeVal2,url)
        dateVar=dateVar+timedelta(days=1)
        
        
    

def pageNavigation(tr,tr2,td,td2,timeVal1,timeVal2,url):

    
    browser1.get(url)
    browser1.maximize_window()
  

       
    pickElementDate = browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[1]/div/input").click()
    pickDate = browser1.find_element_by_xpath("html/body/div[6]/div[3]/table/tbody/tr["+str(tr)+"]/td["+str(td)+"]").click()
    pickElementTime = browser1.find_element_by_xpath(".//*[@id='picktime']").click()
    pickTime = browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[2]/div/div[2]/div[3]").click()



    pickElementDate = browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[3]/div/input").click()
    pickDate = browser1.find_element_by_xpath("html/body/div[7]/div[3]/table/tbody/tr["+str(tr2)+"]/td["+str(td2)+"]").click()
    pickElementTime = browser1.find_element_by_xpath(".//*[@id='picktime2']").click()
    pickTime = browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[4]/div[2]/div[5]").click()

    Location(url)



    
def Location(url):

    if url=="https://www.royalbrothers.in/Bangalore":
        
        array = ["BTM (Linto cafe,Opp Jayadeva Hospital)","East point college (KR Puram)","Electronic City Phase1 (Uniworld )","Hebbal (RMV Extension)","HSR Layout(Near BDA)","Indira Nagar(Near Metro station)","Koramangala (Opp Forum Mall)","M. S. Engg College(Near Airport)","Marathahalli bridge(Sherlock pub)","NMIT (Yelahanka)","Reva University (Airport road)","Whitefield (Ginger Hotel, opp SAP labs)"]

        i=0
        print array[i]
        pickLocation1 = browser1.find_element_by_xpath(".//*[@value="+"\""+array[i]+"\""+"]").click()
        searchButton =   browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[6]/div/input").click()
        page_info()
        i+=1
        while i< len(array):
            
            print array[i]
            pickLocation1 = browser1.find_element_by_xpath(".//*[@value="+"\""+array[i]+"\""+"]").click()
            page_info()
            changeSearch =   browser1.find_element_by_xpath(".//*[@id='sp_search_form']/div/div[7]/div/input").click()
            i=i+1


    elif url=="https://www.royalbrothers.in/Chikballapur":
        
        array = ["SJCIT "]

        i=0
        print array[i]
        pickLocation1 = browser1.find_element_by_xpath(".//*[@value="+"\""+array[i]+"\""+"]").click()
        searchButton =   browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[6]/div/input").click()
        page_info()
       

    elif url=="https://www.royalbrothers.in/Chikmagalur":
        
        array = ["KSRTC Bus station (AIT Circle) "]

        i=0
        print array[i]
        pickLocation1 = browser1.find_element_by_xpath(".//*[@value="+"\""+array[i]+"\""+"]").click()
        searchButton =   browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[6]/div/input").click()
        page_info()


    elif url=="https://www.royalbrothers.in/Coorg":
        
        array = ["Raja Seat Road (Near LIC Office)"]

        i=0
        print array[i]
        pickLocation1 = browser1.find_element_by_xpath(".//*[@value="+"\""+array[i]+"\""+"]").click()
        searchButton =   browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[6]/div/input").click()
        page_info()


    elif url=="https://www.royalbrothers.in/Mangalore":
        
        array = ["Jyothi Circle (Near KSRTC bus station)"]

        i=0
        print array[i]
        pickLocation1 = browser1.find_element_by_xpath(".//*[@value="+"\""+array[i]+"\""+"]").click()
        searchButton =   browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[6]/div/input").click()
        page_info()


    elif url=="https://www.royalbrothers.in/Manipal":
        
        array = ["Manipal Motors (Udupi Road)","Tiger Circle(RSB Bhavan)"]

        i=0
        print array[i]
        pickLocation1 = browser1.find_element_by_xpath(".//*[@value="+"\""+array[i]+"\""+"]").click()
        searchButton =   browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[6]/div/input").click()
        page_info()
        i+=1
        while i< len(array):
            
            print array[i]
            pickLocation1 = browser1.find_element_by_xpath(".//*[@value="+"\""+array[i]+"\""+"]").click()
            page_info()
            changeSearch =   browser1.find_element_by_xpath(".//*[@id='sp_search_form']/div/div[7]/div/input").click()
            i=i+1


    elif url=="https://www.royalbrothers.in/Mysore":
        
        array = ["Hotel Kalyani(Near Infosys)","Hotel Sepoy Grande(MG Road)","Railway Station(Near A2B Hotel)","Windflower Resort & Spa (Nazarbad)"]

        i=0
        print array[i]
        pickLocation1 = browser1.find_element_by_xpath(".//*[@value="+"\""+array[i]+"\""+"]").click()
        searchButton =   browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[6]/div/input").click()
        page_info()
        i+=1
        while i< len(array):
            
            print array[i]
            pickLocation1 = browser1.find_element_by_xpath(".//*[@value="+"\""+array[i]+"\""+"]").click()
            page_info()
            changeSearch =   browser1.find_element_by_xpath(".//*[@id='sp_search_form']/div/div[7]/div/input").click()
            i=i+1
        Location = browser1.find_element_by_xpath(".//*[@selected='selected']").click()
        page_info()


    elif url=="https://www.royalbrothers.in/Udupi":
        
        array = ["Hotel Mathura( SriKrishna temple parking)"]

        i=0
        print array[i]
        pickLocation1 = browser1.find_element_by_xpath(".//*[@value="+"\""+array[i]+"\""+"]").click()
        searchButton =   browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[6]/div/input").click()
        page_info()


    elif url=="https://www.royalbrothers.in/Vijaywada":
        
        array = ["Benz Circle"]

        i=0
        print array[i]
        pickLocation1 = browser1.find_element_by_xpath(".//*[@value="+"\""+array[i]+"\""+"]").click()
        searchButton =   browser1.find_element_by_xpath(".//*[@id='hp_search_form']/ul/li[6]/div/input").click()
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

    bike_info=soup.find_all("div",{"class":"item-details"})
   
    for a in bike_info:
        
   
        print(a.text)
        
        
    
    

Location1= "https://www.royalbrothers.in/Bangalore"
dateNavigation(Location1)
Location2= "https://www.royalbrothers.in/Chikballapur"
dateNavigation(Location2)
Location3= "https://www.royalbrothers.in/Chikmagalur"
dateNavigation(Location3)
Location4= "https://www.royalbrothers.in/Coorg"
dateNavigation(Location4)
Location5= "https://www.royalbrothers.in/Mangalore"
dateNavigation(Location5)
Location6= "https://www.royalbrothers.in/Manipal"
dateNavigation(Location6)
Location7= "https://www.royalbrothers.in/Mysore"
dateNavigation(Location7)
Location8= "https://www.royalbrothers.in/Udupi"
dateNavigation(Location8)
Location9= "https://www.royalbrothers.in/Vijaywada"
dateNavigation(Location9)


'''
    for value in bike_title:       
        a=" ".join(value.text.split())
        final= a.encode("ascii","replace")
        k,v=final.split("Free")
        d[k]=v.split(':')
        l.append(d)
'''

   
       
   
