from django.db import models

# Create your models here.


from django.db import models

class Employee(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)

	def __str__(self) -> str:
		return self.name
