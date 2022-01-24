
from django.db import models

# Create your models here.

class EmployeeDetails(models.Model):
    name = models.CharField(max_length=20)
    email_id = models.EmailField()
    salary = models.IntegerField()
    img = models.ImageField(upload_to='Images/')
    intern_status = models.BooleanField(default=False)
