from django.urls import path
from . import views

urlpatterns = [
	path('', views.firstpage, name="home"),
	path('ok', views.Details, name="ok"),
	path('new', views.restdetails, name="new"),
	path('next', views.restip, name="next"),
	path('success', views.park, name="success"),
	path('done', views.rates, name="done"),
	path('wow', views.resibo, name="wow"),
	path('edit/<int:id>', views.edit),
	path('update/<int:id>', views.update),
	path('delete/<int:id>', views.destroy),
	
]