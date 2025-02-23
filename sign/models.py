from django.db import models

# Create your models here.

# Event Table
class Event(models.Model):
    name = models.CharField(max_length=100, verbose_name="Event Title") 
    limit = models.IntegerField(verbose_name="Participant Limit")  
    status = models.BooleanField(default=True, verbose_name="Active Status")  
    address = models.CharField(max_length=200, verbose_name="Address") 
    start_time = models.DateTimeField('Event Time')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Creation Time") 

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-start_time']
        verbose_name = "Event"
        verbose_name_plural = "Events"
    
# Guest Table
class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Related Event") 
    realname = models.CharField(max_length=64, verbose_name="Real Name") 
    phone = models.CharField(max_length=16, verbose_name="Phone Number") 
    email = models.EmailField(verbose_name="Email Address") 
    sign = models.BooleanField(default=False, verbose_name="Sign-in Status") 
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Creation Time") 

    def __str__(self):
        return self.realname

    class Meta:
        unique_together = ("event", "phone")
        ordering = ['create_time']
        verbose_name = "Guest"
        verbose_name_plural = "Guests"