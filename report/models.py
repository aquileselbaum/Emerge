from django.db import models

class Report(models.Model):
    location = models.CharField(max_length=255)
    description = models.TextField()
    emergencyForMe = models.BooleanField(default=False)
    emergencyForSomeoneElse = models.BooleanField(default=False)
    resolved = models.BooleanField(default=False)
    priority = models.IntegerField(default=5)
    actionResponse = models.TextField(blank=True, null=True) 
    suppliesResponse = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title

