from django.db import models
import datetime

class Ad(models.Model):
	type = models.CharField(max_length=16)
	title = models.CharField(max_length=128)
	description = models.TextField()
	price = models.IntegerField()
	date = models.DateTimeField('date published')
	image_url = models.URLField()
	saved = models.BooleanField()
	def __unicode__(self):
                return self.title
