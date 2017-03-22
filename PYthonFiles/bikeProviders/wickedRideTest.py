# -*- coding: utf-8 -*-
import selenium
import unittest, time, re

class wickedRideTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "C:\Python27\Scripts\chromedriver.exe", "http://wickedride.com/")
        self.selenium.start()
    
    def test_wicked_ride(self):
        sel = self.selenium
        sel.open("/booking/choose-models?start_date=13+Feb+2017&start_time=13%3A00&end_date=15+Feb+2017&end_time=13%3A00&city_id=1&_token=4LxlslDKuKfwuIKeqqWizDKnd4dQ3hLuvXCLEWPf")
        sel.click("css=span.edit-button")
        sel.click("//tr[3]/td[3]/div")
        sel.click("//div[4]/div[2]/div/div/div[2]")
        sel.click("//div[5]/div/div[2]/table/tbody/tr[3]/td[5]")
        sel.click("//div[6]/div[2]/div/div/div[2]")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
