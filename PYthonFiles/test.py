import time
from datetime import datetime, timedelta
import calendar
import numpy as np
import re

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
test=soup.find_all("div",{"class","rm_container"})
test2=soup.find_all("a")
print(test[0])
#print(soup.prettify())
#for i in range(30):
#  print("\n \n ")
# print(test[i])

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
'''
b="Honda Activa 3G Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: HSR Layout Book', Hero Maestro Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: HSR Layout Book', u'Hero Maestro Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: Horamavu/Banaswadi Book', u'Hero Maestro Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: RT Nagar Book', u'Hero Maestro Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: Koramangala Book', u'Hero Maestro Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: Mahadevpura Book', u'Hero Duet Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: HSR Layout Book', u'Honda Activa 3G Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: RT Nagar Book', u'Mahindra Gusto DX Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: HSR Layout Book', u'BTWIN Rockrider 500 Total Fare: Rs. 450 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: Unlimited Pickup location: Horamavu/Banaswadi Book', u'Honda Activa 3G Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: Horamavu/Banaswadi Book', u'Firefox Target D21 Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: Unlimited Pickup location: RT Nagar Book', u'BTWIN Rockrider 340 Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: Unlimited Pickup location: Horamavu/Banaswadi Book', u'BTWIN Rockrider 340 Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: Unlimited Pickup location: RT Nagar Book', u'RE Bullet 500 Total Fare: Rs. 1100 Duration: 16 hour(s) Security deposit: Rs. 2500 KM limit: 300 KM | Extra KM Charges: Rs. 3/KM Pickup location: Horamavu/Banaswadi Book', u'Hero Duet Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: Mahadevpura Book', u'RE Classic Desert Storm 500 Total Fare: Rs. 1100 Duration: 16 hour(s) Security deposit: Rs. 2500 KM limit: 300 KM | Extra KM Charges: Rs. 3/KM Pickup location: RT Nagar Not Available', u'Honda Dio Total Fare: Rs. 360 Duration: 16 hour(s) Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: HSR Layout Not Available', u'RE Himalayan Total Fare: Rs. 1400 Duration: 16 hour(s) Security deposit: Rs. 2500 KM limit: 300 KM | Extra KM Charges: Rs. 3/KM Pickup location: RT Nagar Not Available', u'RE Thunderbird 500 Total Fare: Rs. 1100 Duration: 16 hour(s) Security deposit: Rs. 2500 KM limit: 300 KM | Extra KM Charges: Rs. 3/KM Pickup location: RT Nagar Not Available', u'RE Continental GT 535 Total Fare: Rs. 1200 Duration: 16 hour(s) Security deposit: Rs. 2500 KM limit: 300 KM | Extra KM Charges: Rs. 3/KM Pickup location: RT Nagar Not Available"
a='Security deposit: Rs. 1000 KM limit: 120 KM | Extra KM Charges: Rs. 3/KM Pickup location: Mahadevpura Book'
k,v=a.split(':')
print(k,v)
#print(a)
#myDict=dict((k.strip(), v.strip()) for k,v in (re.split('Total Fare',item) for item in b.split(',') ))
'''
dict((k.strip(), v.strip()) for k,v in 
              (item.split('-') for item in s.split(',')))
'''
#print(len(myDict))


