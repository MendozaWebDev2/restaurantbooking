from django.shortcuts import render, HttpResponse
from .models import Item

def mainpage(request):
	
	if request.method == 'POST':
		Name = request.POST['Name']
		Name1 = request.POST['Name1']
		Address = request.POST['Address']
		Date = request.POST['Date']
		Submit = request.POST['Submit']
		
		
		den = Item()
		den.Name = Name
		den.Name1 = Name1
		den.Address = Address
		den.Date = Date
		den.Submit = Submit
		den.save()

	return render(request, 'mainpage.html')

def Page (request):

	den = Item.objects.all().order_by('Name')
	return render(request,'Add.html',{'den': den})

# Create your views here.
