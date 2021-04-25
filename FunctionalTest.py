from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')

'''class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def test_browser_test(self):
		browser.get('http://127.0.0.1:8000')

	def test_browser_title(self): 
		self.browser.get('http://localhost:8000')
		self.assertIn('Add Suggested Place', self.browser.title)

		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Add Suggested Place', headerText)

		input1= self.browser.find_element_by_id('in1').text
		self.assertIn('Name', input1)
		name = self.browser.find_element_by_id('Name').send_keys("Eden Mendoza")
		time.sleep(2)

		input2= self.browser.find_element_by_id('in2').text
		self.assertIn('Name of Suggested Restaurant or Site', input2)
		name = self.browser.find_element_by_id('Name1').send_keys("Batang 9Teas-Milk Tea")
		time.sleep(2)

		input3= self.browser.find_element_by_id('in3').text
		self.assertIn('Address of Suggested Restaurant or Site', input3)
		name = self.browser.find_element_by_id('Address').send_keys("Brgy. San Esteban, Dasmarinas")
		time.sleep(2)

		input4= self.browser.find_element_by_id('in4').text
		self.assertIn('Date', input)
		name = self.browser.find_element_by_id('Date').send_keys("24/04/2021")
		time.sleep(2)


if __name__== '__main__':
	unittest.main(warnings='ignore')'''