from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from MyWeb.views import mainpage
from django.urls import resolve
from MyWeb.models import Item

class MainpageTest(TestCase):

	def html_index_root_mainpage_pwede_din_homepage_basta(self):
		found = resolve('/')
		self.assertEqual(found.func, mainpage)

		
	def test_index_returns_correct_view(self):
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
		self.assertIn('<title>Add Suggested Place</title>', html)
		self.assertIn('</head>', html)
		self.assertIn('<body bgcolor="gainsboro">', html)
		self.assertIn('<div class="form">', html)
		self.assertIn('<form class="form" action="" method="post">' ,html)
		self.assertIn('<div class="heading">', html)
		self.assertIn('<h1 style="color: forestgreen">Add Suggested Place</h1>', html)
		self.assertIn('</div>', html)
		self.assertIn('<p id=in1>Name</p>', html)
		self.assertIn('<input size="40" type="text" id=Name name="Name" placeholder="Fisrtname, Lastname">', html)
		self.assertIn('<p id=in2>Name of Suggested Restaurant or Site</p>', html)
		self.assertIn('<input size="40" type="text" id=Name1 name="Name1" placeholder="Type Here">', html)
		self.assertIn('<p id=in3>Address of Suggested Restaurant or Site</p>', html)
		self.assertIn('<input size="40" type="text" id=Address name="Address" placeholder="Type Here">', html)
		self.assertIn('<p id=in4>Date</p>', html)
		self.assertIn('<input  style="height: 35px; width: 200px; " type="date" id="Date" placeholder="Date" name="Date">', html)
		self.assertIn('<br>', html)
		self.assertIn('<input type="submit" id="Submit" name="Submit" value="Submit">', html)
		self.assertIn('</form>', html)
		self.assertIn('</body>', html)
		self.assertIn('</html>', html)


		self.assertTrue(html.strip().endswith('</html>'))

class ORM_Save(TestCase):
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
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 4)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		self.assertEqual(Item1.Name, 'Eden Mendoza')
		self.assertEqual(Item2.Name1, 'Unli Wings')
		self.assertEqual(Item3.Address, 'Palipran 2, Dasmarinas City, Cavite')
		self.assertEqual(Item4.Date, '2021-04-26')
