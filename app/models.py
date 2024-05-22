from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=25,blank=False)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25,blank=False)

    def __str__(self):
        return self.name