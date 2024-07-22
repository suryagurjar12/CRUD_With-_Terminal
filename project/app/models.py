from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_city=models.CharField(max_length=50)
    stu_email=models.EmailField()
    
    def __str__(self):
        return self.stu_name
    