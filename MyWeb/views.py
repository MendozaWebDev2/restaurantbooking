from django.shortcuts import redirect, render
from .models import Booking, BookingDetails, Tip, Parking, Ratings

def firstpage(request):

	return render(request,'Booking.html')

def Details(request):

	customerId=Booking.objects.create(
		Name = request.POST['Name'],
		Name1 = request.POST['Name1'],
		Num = request.POST['Num'],
		Address = request.POST['Address'],
		)

	return render(request,'BookingDetails.html')
	# return redirect('ok')

def secondpage(request):

	return render(request,'BookingDetails.html')

def restdetails(request):

	customerId=BookingDetails.objects.create(
		Rname = request.POST['Rname'],
		Nums= request.POST['Nums'],
		date = request.POST['date'],
		time = request.POST['time'],
		cnum = request.POST['cnum'],
		cname = request.POST['cname'],
		cdate = request.POST['cdate'],
		ccode = request.POST['ccode'],

		)

	return render(request,'Tip.html')
	# return redirect('third')

def thirdpage(request):

	return render(request,'Tip.html')

def restip(request):

	customerId=Booking.objects.create(
		AmountofTip = request.POST['AmountofTip'],
		)

	return render(request,'Parking.html')

def fourthpage(request):

	return render(request,'Parking.html')

def park(request):

	customerId=Booking.objects.create(
		Ask = request.POST['Ask'],
		Ehours = request.POST['Ehours'],
		)

	return render(request,'Ratings.html')

def fifthpage(request):

	return render(request,'Ratings.html')

def rate(request):

	customerId=Booking.objects.create(
		rating = request.POST['rate'],
		comments = request.POST['comments'],
		)

	return render(request,'Ratings.html')





