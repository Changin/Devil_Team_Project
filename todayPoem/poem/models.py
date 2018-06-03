from django.db import models

# Create your models here.
class Poetry(models.Model):
	poem_title = models.CharField(max_length=30,default='TITLE')
	poem_text = models.CharField(max_length=500)
	poem_writer = models.CharField(max_length=10)

	def __str__(self):
		return self.poem_title