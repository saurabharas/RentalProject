#from webscraping import webkit
#w = webkit.WebkitBrowser(gui=True)
#w.get('http://webscraping.com')
#w.fill('input[id=search_form_input_homepage]', 'sitescraper')
# take screenshot of browser
#w.wait(20)

#w.screenshot('rentmojo.jpg')
# click search button 
#w.click('input[id=search_button_homepage]')
# wait on results page
#w.wait(15)
# take another screenshot
#w.screenshot('rentmojo_results.jpg')

import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class Screenshot(QWebView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)

    def capture(self, url, output_file):
        self.load(QUrl(url))
        #time.sleep(25)
        self.wait_load()
        # set to webpage size
        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())
        # render image
        image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
        painter = QPainter(image)
        frame.render(painter)
        painter.end()
        print 'saving', output_file
        image.save(output_file)

    def wait_load(self, delay=10):
        # process app events until page loaded
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False

    def _loadFinished(self, result):
        self._loaded = True

s = Screenshot()
s.capture('https://www.rentomojo.com/bangalore?utm_source=bing&utm_medium=cpc&utm_campaign=brand_search', 'website7.png')
#s.capture('http://www.rentsetgo.co/pune/commuterbikesonrent/honda-activa/2981?gclid=Cj0KEQiA5bvEBRCM6vypnc7QgMkBEiQAUZftQPD8lVSOsyNghsTDHbM-uxZBsXAj5WCz6AmsQWMFRkgaApPW8P8HAQ', 'blog1.png')
