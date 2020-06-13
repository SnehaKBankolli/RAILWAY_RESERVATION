from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Train(models.Model):
    train_name =       models.CharField(max_length=200)
    source     =       models.CharField(max_length=200)
    destination=       models.CharField(max_length=200)
    date       =       models.DateField("Date", default=datetime.date.today)
    time       =       models.TimeField(auto_now=False, auto_now_add=False)
    number     =       models.IntegerField(default=60)
    cost       =       models.IntegerField(default=0)
    
    def __str__(self):
        return self.train_name

class Ticket(models.Model):
    ticket_name = models.CharField(max_length=200)
    train       = models.ForeignKey(Train, on_delete=models.CASCADE)
    number      = models.IntegerField(default=0)
    cost        = models.IntegerField(default=0)
    gender      = models.CharField(max_length=200, default="male")
    time        = models.TimeField(auto_now=False, auto_now_add=False)
    date        = models.DateField("Date", default=datetime.date.today)


    def __str__(self):
        return self.ticket_name