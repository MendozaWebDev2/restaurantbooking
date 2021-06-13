from django.db import models


class Booking(models.Model):
	Name = models.CharField(max_length=50, null=True)
 	#first name
	Name1 = models.CharField(max_length=50, null=True)
	#last name
	Num = models.IntegerField(null=True)
	#Conctact number
	Address = models.CharField(max_length=50, null=True)
 	#addres


	def __str__(self):
 		return self.Name

class BookingDetails(models.Model):
	costumerId = models.ForeignKey(Booking, default=None, on_delete=models.CASCADE, null=True)
 	#UniqueName of costumer
	Rname = models.CharField(max_length=50, null=True)
 	#restaurant name
	Nums = models.IntegerField(null=True)
	#number of seat
	date = models.DateTimeField(max_length=50, null=True)
	#date
	time = models.TimeField(max_length=50, null=True)
 	#time
	cnum = models.CharField(max_length=50, null=True)
	#CardNo.
	cname = models.CharField(max_length=50, null=True)
	#CardHoldername
	cdate = models.CharField(max_length=50, null=True)
 	#ExpirationDate
	ccode = models.CharField(max_length=50, null=True)

	def __str__(self):
 		return self.Rname


class Tip(models.Model):
	costumerId = models.ManyToManyField(Booking)
 	#UniqueName of costumer
	AmountofTip = models.IntegerField(null=True)
 	#amount
	add = models.IntegerField(null=True)

	def __str__(self):
 		return self.AmountofTip

class Parking(models.Model):
	costumerId = models.ManyToManyField(Booking)
	Ask = models.CharField(max_length=50, null=True)
	#Ask if they have car or motorcyle
	Ehours = models.CharField(max_length=50, null=True)
	#estimated hours of parking
	Kind = models.CharField(max_length=50, null=True)
	#kind of vehicle
	def __str__(self):
		return self.Ask

class Ratings(models.Model):
	costumerId = models.ManyToManyField(Booking)
 	#UniqueName of costumer
	rate = models.CharField(max_length=50, null=True)
 	#Rate
	comments = models.TextField(max_length=500, null=True)
	#Comments&Suggestion

	def __str__(self):
 		return self.rate

