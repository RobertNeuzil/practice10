from django.db import models


class Poll(models.Model):
	
	text = models.CharField(max_length=255)
	pub_date = models.DateField()

	def __str__(self):
		return f'{self.text[:20]}'
# Create your models here.