from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.




class ReportingTo(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)

class Employee(models.Model):
    
    name=models.CharField(max_length=100)
    empid=models.CharField(max_length=600)
    designation=models.CharField(max_length=100,choices=[('Developer','Developer'),('Manager','Manager')])
    reportingto=models.ForeignKey(ReportingTo,on_delete=models.CASCADE,null=True,blank=True)
    


@receiver(post_save,sender=Employee)
def add_to_ReportingTo(sender,instance,**kwargs):
    if instance.designation=='Manager':
        ReportingTo.objects.create(name=instance.name)