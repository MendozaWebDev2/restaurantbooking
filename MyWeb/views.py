from django.shortcuts import render

def MainPage(request):
	return render(request, 'mainpage.html')

# Create your views here.
