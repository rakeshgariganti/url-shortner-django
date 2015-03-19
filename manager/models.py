from django.db import models
import admin
# Create your models here.

class Url(models.Model):
	longurl = models.URLField()
	short = models.CharField(max_length=6)