from django.urls import resolve
from django.test import TestCase
from MyWeb.views import MainPage

class HomePageTest(TestCase):

	def test_root_url_resolve_to_mainpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, MainPage)

	'''def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		string_html = render_to_string('mainpage.html')
		self.assertEqual(html, string_html)
		self.assertTemplateUsed(response, 'mainpage.html')'''

	'''def test_root_url_resolves_to_mainpage_views(self):
		found = resolve('/')
		self.assretEqual(found.func, Mainpage)'''

	'''def test_mainpage_returns_correct_views(self):
		request = HttpRequest()
		response = MainPage(request)
		#html = response.content.decode(utf8)
		#string.html = render_to_string('mainpage.html')
		#self.assrtEqual(html, string_html)'''

	'''def test_mainpage_returns_correct_views(self):
		request = HttpRequest()
		response = MainPage(request)
		#html = response.content.decode('utf8')
		self.assertTrue(html.strip().startswitch('<html>'))
		self.assertIn('<title>Add Place</title>', html)
		self.assertTrue(html.strip().endswitch('</html>'))'''

# Create your tests here.
