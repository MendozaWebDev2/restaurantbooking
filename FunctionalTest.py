from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

'''browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')'''

class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def test_browser_test(self):
		'''browser.get('http://127.0.0.1:8000')'''

	def test_browser_title(self): 
		self.browser.get('http://localhost:8000')
		self.assertIn('Add Place', self.browser.title)

		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Add Place', headerText)

		input1= self.browser.find_element_by_id('in1').text
		self.assertIn('Name', input1)
		name = self.browser.find_element_by_id('Name').send_keys("Eden Mendoza")

		input2= self.browser.find_element_by_id('in2').text
		self.assertIn('Name of Suggested Restaurant or Site', input2)
		name = self.browser.find_element_by_id('Name1').send_keys("Batang 9Teas-Milk Tea")

		input3= self.browser.find_element_by_id('in3').text
		self.assertIn('Address of Suggested Restaurant or Site', input3)
		name = self.browser.find_element_by_id('Address').send_keys("Brgy. San Esteban, Dasmarinas")


		'''inputbox.send_keys('eden')
		inputbox.send_keys('Keys.ENTER')
		time.sleep(1)
		table = self.browser.find_element_by_id('idListTable')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(any(row.text == '1:Twice'))'''	



if __name__== '__main__':
	unittest.main(warnings='ignore')