import time
from datetime import datetime, timedelta
import calendar
import re
from bs4 import BeautifulSoup
'''
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from bs4 import BeautifulSoup

class Render(QWebPage):
  def __init__(self, url):
    self.app = QApplication(sys.argv)
    QWebPage.__init__(self)
    self.loadFinished.connect(self._loadFinished)
    self.mainFrame().load(QUrl(url))
    self.app.exec_()

  def _loadFinished(self, result):
   # self.frame = self.mainFrame()
    self.app.quit()

'''

'''
url = 'http://pycoders.com/archive/'
r = Render("https://www.rentomojo.com/bangalore/bikes-on-rent")
#html = r.frame.totml()
html = r.mainFrame().toHtml()
#formatted_result = str(html.encode("utf-8"))
#print(html)
#print(html.encode("utf-8"))
soup=BeautifulSoup(html,"lxml")
#print(soup)
#test=soup.find_all("div",{"class","rm_container"})
#test2=soup.find_all("a")
#print(test[0])
#print(soup.prettify())
#for i in range(30):
#  print("\n \n ")
# print(test[i])
<<<<<<< HEAD
print(datetime.now().isoweekday())
print(int(datetime.now().strftime('%H'))==range(1,17))
=======

a=u'RS 6912'
a.encode("UTF-8")
newstr = a.replace("RS ", "")
print(datetime.now().weekday()==6)
print(datetime.now()+timedelta(days=6))


def get_week_of_month(year, month, day):
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] + 1
    return(week_of_month)

print(get_week_of_month(2017,3,1))

d=datetime.now()
print(d.day)

b="Honda Activa 3G Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: HSR Layout Book', Hero Maestro Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: HSR Layout Book', u'Hero Maestro Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: Horamavu/Banaswadi Book', u'Hero Maestro Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: RT Nagar Book', u'Hero Maestro Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: Koramangala Book', u'Hero Maestro Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: Mahadevpura Book', u'Hero Duet Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: HSR Layout Book', u'Honda Activa 3G Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: RT Nagar Book', u'Mahindra Gusto DX Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: HSR Layout Book', u'BTWIN Rockrider 500 Total Fare: Rs. 450 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: Unlimited Pickup location: Horamavu/Banaswadi Book', u'Honda Activa 3G Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: Horamavu/Banaswadi Book', u'Firefox Target D21 Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: Unlimited Pickup location: RT Nagar Book', u'BTWIN Rockrider 340 Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: Unlimited Pickup location: Horamavu/Banaswadi Book', u'BTWIN Rockrider 340 Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: Unlimited Pickup location: RT Nagar Book', u'RE Bullet 500 Total Fare: Rs. 1100 Duration: 16 hour(s) Security deposit: Rs. 2500 KM limit: 300 KM | Extra KM Charges: Rs. 3/KM Pickup location: Horamavu/Banaswadi Book', u'Hero Duet Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: Mahadevpura Book', u'RE Classic Desert Storm 500 Total Fare: Rs. 1100 Duration: 16 hour(s) Security deposit: Rs. 2500 KM limit: 300 KM | Extra KM Charges: Rs. 3/KM Pickup location: RT Nagar Not Available', u'Honda Dio Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: HSR Layout Not Available', u'RE Himalayan Total Fare: Rs. 1400 Duration: 16 hour(s) Security deposit: Rs. 2500 KM limit: 300 KM | Extra KM Charges: Rs. 3/KM Pickup location: RT Nagar Not Available', u'RE Thunderbird 500 Total Fare: Rs. 1100 Duration: 16 hour(s) Security deposit: Rs. 2500 KM limit: 300 KM | Extra KM Charges: Rs. 3/KM Pickup location: RT Nagar Not Available', u'RE Continental GT 535 Total Fare: Rs. 1200 Duration: 16 hour(s) Security deposit: Rs. 2500 KM limit: 300 KM | Extra KM Charges: Rs. 3/KM Pickup location: RT Nagar Not Available"
a='Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: Mahadevpura Book'
k,v=a.split(':')
print(k,v)
#print(a)
#myDict=dict((k.strip(), v.strip()) for k,v in (re.split('Total Fare',item) for item in b.split(',') ))

dict((k.strip(), v.strip()) for k,v in 
              (item.split('-') for item in s.split(',')))


#print(len(myDict))
'''
#nested dictionary
'''
d={}
d['Bajaj Avenger cruiz 220']={}
d['Bajaj Avenger cruiz 220']['Koramangala (opp. Forum Mall)']={'Advance':500,'WeekDayRate/hr':35,'WeekDayRate/day':700,'WeekEndRate/hr':45,'WeekEndRate/day':800}
d['Bajaj Avenger cruiz 220']['Koramangala (opp. Forum Mall)2']={'Advance':500,'WeekDayRate/hr':35,'WeekDayRate/day':700,'WeekEndRate/hr':45,'WeekEndRate/day':800}

d={'Bajaj Avenger cruiz 220':
                    {'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}},

   'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},

                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}


    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}


    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}


    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}


    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}


    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}


    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}



    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}


    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}


    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}


    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}

    'Kawasaki Z800':{'Koramangala (opp. Forum Mall)': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35},
                    'Koramangala (opp. Forum Mall)2': {'WeekEndRate/hr': 45, 'Advance': 500, 'WeekDayRate/day': 700, 'WeekEndRate/day': 800, 'WeekDayRate/hr': 35}}



   }


for k,v in d.items():
    for k1,v1 in v.items():
        for k2,v2 in v1.items():
            print(v2)



def costCalc(pickUpTotal,dropTotal,WeekDayRateHr,WeekDayRateDay, WeekEndRateHr, WeekEndRateDay):
    dateDiff=dropTotal-pickUpTotal
    totalHr=dateDiff.total_seconds()/3600
    pickVar=pickUpTotal
    dropVar=dropTotal
    qut=int(totalHr/24)
    rem=totalHr%24
    i=0
    weekdayCount=0
    weekendCount=0
    remDropHr=0
    cost=0
    while(i<qut):
        if(pickVar.weekday()<=3):
            weekdayCount=weekdayCount+1
        else:
            weekendCount=weekendCount+1
        print(pickVar)
        pickVar=pickVar+timedelta(days=1)
        print(weekdayCount,weekendCount,rem)
        i=i+1
    print(totalHr)
    if(totalHr<21):
        if(pickUpTotal.weekday()<=3):
            hrCost=totalHr*WeekDayRateHr
        else:
            hrCost=totalHr*WeekEndRateHr
    elif(rem>=21 and rem<24):
        if(pickUpTotal.weekday()<=3):
            hrCost=WeekDayRateDay
        else:
            hrCost=WeekEndRateDay
    else:
        if(dropVar.weekday()<=3):
            hrCost=rem*WeekDayRateHr
        else:
            hrCost=rem*WeekEndRateHr
    cost=weekdayCount*WeekDayRateDay+weekendCount*WeekEndRateDay+hrCost
    
    print(cost)
    
    
    
pickUpTotal=datetime.strptime('24-02-2017 12', "%d-%m-%Y %H")                                                                            
dropTotal=datetime.strptime('26-02-2017 9', "%d-%m-%Y %H")

pickUpDate=pickUpTotal.strftime('%d')                                                                            
dropDate=dropTotal.strftime('%d')

pickUpTime=pickUpTotal.strftime('%H')                                                                            
dropTime=dropTotal.strftime('%H')


costCalc(pickUpTotal,dropTotal,35,700,45,850)



algo:
q=days
r=hr
diff=4
while 


#Filtering the String COntent
listTest=['Bike Make: Suzuki','Free KM: 5KM Per Hour','Cost Per Hour: 16.65 INR','Cost Per Hour At Weekend: 19.035 INR','Cost Per Extra Hour: 200 INR','Cost Per Extra KM: 3 INR']
myString='hider3554'
#print(myString.isalpha())
#print(myString.isalnum())

print(listTest[0].split(':')[1])
for val in listTest[1:len(listTest)]:
    a=val.split(':')[1]
    b=re.findall(r"[-+]?\d*\.\d+|\d+", a)
    print(b)
        
'''

soup = BeautifulSoup('<div class="thumbnail col-lg-10 col-md-10 col-sm-10" id="model_1"><div class="row" style="padding-top: 15px"><div class="col-lg-5 col-md-5 col-sm-5" style=""><div class="row"><div class="text-center col-lg-12 col-md-12 col-sm-12"><span class="" style="font-size:16px; font-weight: bold;">06 mar 2017 15:00</span><span class="" style="font-size:17px; font-weight: bold;padding-right:38px;padding-left:38px;">TO</span><span class="" style="font-size:16px; font-weight: bold;">07 mar 201717:00</span>',"html.parser")
tag = soup.prettify()

print(tag)
























>>>>>>> 2ef7119624674e3f1410f9caf08d61a367190008
