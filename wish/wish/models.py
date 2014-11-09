from django.db import models

class Bank(models.Model):
    id = models.IntegerField()
    sku = models.CharField(max_length=64)
    name = models.CharField(max_length=512)
    url = models.CharField(max_length=1024)
    emi = models.FloatField()
    months = models.CharField(max_length=4)
#    docfile = models.FileField(upload_to='images/%Y/%m/%d')

class List(models.Model):
	id = models.IntegerField()
	semid = models.IntegerField()
	name = models.CharField(max_length=64)