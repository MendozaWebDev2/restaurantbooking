from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

# from django.test import TestCase
# from django.http import HttpRequest
# from django.template.loader import render_to_string
# from app.views import Index
# from app.views import NextPage
# from django.urls import resolve
# #For Models testing
# from app.models import Details, User
# from django.urls import reverse

class PageTest(LiveServerTestCase):

	
	def setUp(self):
		self.browser = webdriver.Firefox()
		

	def test_browser_title(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Restaurant Dine-In Booking', self.browser.title)

		denText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Restaurant Dine-In Booking', denText)

		p1 = self.browser.find_element_by_tag_name('p').text
		self.assertIn('Name', p1)

		p2 = self.browser.find_element_by_id('in2').text
		self.assertIn('Restaurant', p2)

		p3 = self.browser.find_element_by_id('in3').text
		self.assertIn('Address', p3)

		p4 = self.browser.find_element_by_id('in4').text
		self.assertIn('Date', p4)

		p5 = self.browser.find_element_by_id('in5').text
		self.assertIn('Time', p5)

		form = self.browser.find_element_by_tag_name('form')

		input1 = self.browser.find_element_by_id('Name')  
		self.assertEqual(input1.get_attribute('placeholder'),'Fisrtname, Lastname')
		input1 = self.browser.find_element_by_id('Name').send_keys("Eden Mendoza")
		time.sleep(1)

		input2 = self.browser.find_element_by_id('Name1')  
		self.assertEqual(input2.get_attribute('placeholder'),'Name of Restaurant')
		input2 = self.browser.find_element_by_id('Name1').send_keys("Unli Wings")
		time.sleep(1)

		input3 = self.browser.find_element_by_id('Address')  
		self.assertEqual(input3.get_attribute('placeholder'),'Restaurant Address')
		input3 = self.browser.find_element_by_id('Address').send_keys("Palipran 2, Dasmarinas City, Cavite")
		time.sleep(1)

		date = self.browser.find_element_by_id('Date').click()
		time.sleep(1)
		date = self.browser.find_element_by_id('Date').send_keys("2021-04-26")
		time.sleep(1)

		input5 = self.browser.find_element_by_id('Time')
		self.assertEqual(input5.get_attribute('placeholder'),'HH:MM Am/Pm')
		input5 = self.browser.find_element_by_id('Time').send_keys("12:00 Pm")
		time.sleep(1)

		submit = self.browser.find_element_by_id('Submit').click()
		time.sleep(3)

		self.browser.quit()	
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)

		input1 = self.browser.find_element_by_id('Name')  
		self.assertEqual(input1.get_attribute('placeholder'),'Fisrtname, Lastname')
		input1 = self.browser.find_element_by_id('Name').send_keys("Charles DelaCruz")
		time.sleep(1)

		input2 = self.browser.find_element_by_id('Name1')  
		self.assertEqual(input2.get_attribute('placeholder'),'Name of Restaurant')
		input2 = self.browser.find_element_by_id('Name1').send_keys("Samgyupsal")
		time.sleep(1)

		input3 = self.browser.find_element_by_id('Address')  
		self.assertEqual(input3.get_attribute('placeholder'),'Restaurant Address')
		input3 = self.browser.find_element_by_id('Address').send_keys("Salawag, Dasmarinas City, Cavite")
		time.sleep(1)

		date = self.browser.find_element_by_id('Date').click()
		time.sleep(1)
		date = self.browser.find_element_by_id('Date').send_keys("2021-04-26")
		time.sleep(1)

		input5 = self.browser.find_element_by_id('Time')
		self.assertEqual(input5.get_attribute('placeholder'),'HH:MM Am/Pm')
		input5 = self.browser.find_element_by_id('Time').send_keys("12:00 Pm")
		time.sleep(1)

		submit = self.browser.find_element_by_id('Submit').click()
		time.sleep(1)

		nextpage = self.browser.current_url
		self.assertRegex(nextpage, '/Add/')

		self.browser.quit()







		


# if __name__ == '__main__':
# 	unittest.main()