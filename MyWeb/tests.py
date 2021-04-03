from django.urls import resolve
from django.test import TestCase
from MyWeb.views import MainPage

class HomePageTest(TestCase):

	def test_root_url_resolve_to_mainpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, MainPage)

# Create your tests here.
