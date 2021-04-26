from django.db import models

class Item(models.Model):
	#NAME
	Name = models.CharField(max_length=50, null=True)
	#NAME1
	Name1 = models.CharField(max_length=50, null=True)
	#ADDRESS
	Address = models.CharField(max_length=50, null=True)

	#DATE
	Date = models.DateTimeField(null=True)

	def __str__(self):
		return self.Name