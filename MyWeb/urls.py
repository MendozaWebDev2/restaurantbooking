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
	# path('', views.thirdpage),
	# path('', views.fourthpage),
	# path('', views.fifthpage),

	# path('next', views.BookingDetails, name="next"),
	# path('third', views.BookingFee, name="third"),
	# path('Add/', views.NextPage, name="success"),
	# path('success', views.Nextpage, name="success"),
]