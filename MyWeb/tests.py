from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from MyWeb.views import mainpage
from MyWeb.views import Page
from django.urls import resolve
from MyWeb.models import Item, User
from django.urls import reverse


class MainpageTest(TestCase):

	def html_mainpage_root_mainpage(self):
		found = resolve('/')
		self.assertEqual(found.func, mainpage)
		self.assertEqual(found.func, Add)
		
	def test_mainpage_returns_correct_view(self):
		request = HttpRequest()
		response = mainpage(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'mainpage.html')
		self.assertIn('<html>', html)
		self.assertIn('<head>', html)
		self.assertIn('<meta name="viewport" content="width=device-width, initial-scale=1.0">', html)
		self.assertIn('<title>Restaurant Dine-In Booking</title>', html)
		self.assertIn('</head>', html)
		self.assertIn('<body bgcolor="gainsboro">', html)
		self.assertIn('<div class="form">', html)
		self.assertIn('<form class="form" action="" method="post">' ,html)
		self.assertIn('<div class="heading">', html)
		self.assertIn('<h1 style="color: forestgreen">Restaurant Dine-In Booking</h1>', html)
		self.assertIn('</div>', html)
		self.assertIn('<p id=in1>Name</p>', html)
		self.assertIn('<input size="40" type="text" id=Name name="Name" placeholder="Fisrtname, Lastname">', html)
		self.assertIn('<p id=in2>Restaurant</p>', html)
		self.assertIn('<input size="40" type="text" id=Name1 name="Name1" placeholder="Name of Restaurant">', html)
		self.assertIn('<p id=in3>Address</p>', html)
		self.assertIn('<input size="40" type="text" id=Address name="Address" placeholder="Restaurant Address">', html)
		self.assertIn('<p id=in4>Date</p>', html)
		self.assertIn('<input  style="height: 35px; width: 200px; " type="date" id="Date" placeholder="Date" name="Date">', html)
		self.assertIn('<p id=in5>Time</p>', html)
		self.assertIn('<input size="40" type="text" id=Time name="Time" placeholder="HH:MM Am/Pm">', html)
		self.assertIn('<br>', html)
		self.assertIn('<input type="submit" id="Submit" name="Submit" value="Submit">', html)
		self.assertIn('</form>', html)
		self.assertIn('</body>', html)
		self.assertIn('</html>', html)
		self.assertTrue(html.strip().endswith('</html>'))

class orm_testing_save(TestCase):
	def test_saving(self):
		Item1 = Item()
		Item1.Name = 'Eden Mendoza'
		Item1.save()
		Item2 = Item()
		Item2.Name1 = 'Unli Wings'
		Item2.save()
		Item3 = Item()
		Item3.Address = 'Palipran 2, Dasmarinas City, Cavite'
		Item3.save()
		Item4 = Item()
		Item4.Date = '2021-04-26'
		Item4.save()
		Item5 = Item()
		Item5.Time = '12:00 Pm'
		Item5.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 5)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		self.assertEqual(Item1.Name, 'Eden Mendoza')
		self.assertEqual(Item2.Name1, 'Unli Wings')
		self.assertEqual(Item3.Address, 'Palipran 2, Dasmarinas City, Cavite')
		self.assertEqual(Item4.Date, '2021-04-26')
		self.assertEqual(Item5.Time, '12:00 Pm')

class orm_testing_save1(TestCase):
	def test_saving1(self):
		Item1 = Item()
		Item1.Name = 'Charles DelaCruz'
		Item1.save()
		Item2 = Item()
		Item2.Name1 = 'Samgyupsal'
		Item2.save()
		Item3 = Item()
		Item3.Address = 'Salawag, Dasmarinas City, Cavite'
		Item3.save()
		Item4 = Item()
		Item4.Date = '2021-04-26'
		Item4.save()
		Item5 = Item()
		Item5.Time = '12:00 Pm'
		Item5.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 5)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		self.assertEqual(Item1.Name, 'Charles DelaCruz')
		self.assertEqual(Item2.Name1, 'Samgyupsal')
		self.assertEqual(Item3.Address, 'Salawag, Dasmarinas City, Cavite')
		self.assertEqual(Item4.Date, '2021-04-26')
		self.assertEqual(Item5.Time, '12:00 Pm')

class Views_Test(TestCase):
	def test_views(self):
		Item.objects.create(
			Name='Name', 
			Name1='Name1',
			Address='Address',
			Date='2021-04-26',
			Time='12:00 Pm',
			)
		response = self.client.get('/app/views.mainpage/')

class PageViewTest(TestCase):

	def test_uses_page_template(self):
		viewer = User.objects.create()
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
	def test_uses_home_template(self):
		response = self.client.get('/next/')
	def test_displays_all_list_items(self):
		viewer = User.objects.create()
		Name = Item.objects.create(Name='Name')
		Name1 = Item.objects.create(Name1='Name1')
		Address = Item.objects.create(Address='Address')
		Date = Item.objects.create(Date='2021-04-26')
		Time = Item.objects.create(Time='12:00 Pm')
		response = self.client.get('/')
		self.assertIn('Name', response.content.decode())
		self.assertIn('Name1', response.content.decode())
		self.assertIn('Address', response.content.decode())
		self.assertIn('Date', response.content.decode())
		self.assertIn('Time', response.content.decode())
		Name = Item.objects.get(Name='Name')
		Name1 = Item.objects.get(Name1='Name1')
		Address = Item.objects.get(Address='Address')
		Date = Item.objects.get(Date='2021-04-26')
		Time = Item.objects.get(Time='12:00 Pm')

		self.assertEqual(Item.objects.count(), 5)

class Views(TestCase):
	def setUp(self):
		Name = Name.objects.create()
		Name1 = Item.objects.create()
		Address = Item.objects.create()
		Date = Item.objects.create()
		Time = Item.objects.create()
		
		Item.objects.create(
			Name = 'Eden Mendoza',
			Name1 = 'Unli Wings',
			Address = 'Palipran 2, Dasmarinas City, Cavite',
			Date = '2021-04-26',
			Time='12:00 Pm',
			)
		self.client.post('/Add/', Name='Juan DelaCruz')
		response = self.client.post('/next/')
		self.assertRedirects(response, '/next/')

class Test_models(TestCase):

	def mainpage(self, 
		Name='Name', 
		Name1='Name1', 
		Address='Address', 
		Date='2021-04-26',
		Time='12:00 Pm'):
		
		return User.objects.create()
		return Item.objects.create(
		Name='Name', 
		Name1='Name1', 
		Address='Address', 
		Date='2021-04-26',
		Time='12:00 Pm',)

	def test_whatever_creation(self):
		w = self.mainpage()
		self.assertTrue(isinstance(w, User))
		self.assertFalse(isinstance(w, Item))