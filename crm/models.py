from django.db import models

# Create your models here.
#Employee[id,name,department,salary,location,email]

class Employee(models.Model):
    name = models.CharField(max_length = 200)
    department = models.CharField(max_length = 200)
    salary = models.PositiveIntegerField()
    location = models.CharField(max_length = 200)
    email= models.EmailField(unique = True)
# Create your models here.
