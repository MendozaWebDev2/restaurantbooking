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

	def test_start_list_and_retrieve_it(self): 
		self.browser.get('http://localhost:8000')
		'''self.assertIn('WTG in Dasmarinas', self.browser.title)'''
		headerText = self.browser.find_element_by_tag_name('h1').text
		'''self.assertIn('Group', headerText)'''
		'''inputbox = self.browser.find_element_by_id('idNewEntry')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Group name you have seen')
		inputbox.send_keys('Twice')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		table = self.browser.find_element_by_id('idListTable')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(any(row.text == '1:Twice'))'''



if __name__== '__main__':
	unittest.main(warnings='ignore')


