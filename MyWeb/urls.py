from django.urls import path
from . import views

# urlpatterns = [
# 	path('', views.mainpage,),
# 	path('Add/', views.Page, name="Add"),
# ]

urlpatterns = [
	path('', views.firstpage),
	path('ok', views.Details, name="ok"),
	path('', views.secondpage),
	path('new', views.restdetails, name="new"),
	path('', views.thirdpage),
	path('next', views.restip, name="next"),
	path('', views.fourthpage),
	path('success', views.park, name="success"),
	path('', views.fifthpage),
	path('done', views.rates, name="done"),
	# path('', views.lastpage),
	# path('last', views.info, name="last"),


	# path('done', views.rate, name="done"),

	# path('next', views.BookingDetails, name="next"),
	# path('third', views.BookingFee, name="third"),
	# path('Add/', views.NextPage, name="success"),
	# path('success', views.Nextpage, name="success"),
]