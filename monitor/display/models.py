from django.db import models

class Data(models.Model):
    temp = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    dateandtime = models.DateTimeField(auto_now = False,auto_now_add=True)