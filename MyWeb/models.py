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
	# BankChoices =(
	# 	('1','PayMaya'),
	# 	('2','Gcash Mastercard'),
	# 	('3','BPI'),
	# 	('4','BDO'),
	# 	('5','BSP Prepaid Mastercard'),
	# 	('6','EastWest Prepaid Card'),
	# 	('7','Landbank Cash Card'),
	# 	('8','PNB Prepaid Card'),
	# 	('9','PSBank Prepaid Mastercard'),
	# 	('10','RCBC MyWallet Prepaid Card'),
	# 	('11','Smart Money Card'),
	# 	('12','UnionBank Classic Visa'),
	# 	('13','Metrobank')
	# )
 # 	#Bank choices
	# Choices = models.CharField(max_length=50, default=False, null=True)
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


	def __str__(self):
 		return self.AmountofTip

class Parking(models.Model):
	costumerId = models.ForeignKey(Booking, default=None, on_delete=models.CASCADE, null=True)
	Ask = models.CharField(max_length=50, null=True)
	#Ask if they have car or motorcyle
	Ehours = models.CharField(max_length=50, null=True)
	#estimated hours of parking

	def __str__(self):
		return self.Ask

class Ratings(models.Model):
	costumerId = models.ManyToManyField(Booking)
 	#UniqueName of costumer
	rating =(
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5')
	)
	rate = models.CharField(max_length=50, null=True)

 	#Rate

	comments = models.TextField(max_length=500, null=True)
	#Comments&Suggestion

	def __str__(self):
 		return self.Radio

