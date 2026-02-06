from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    image=models.ImageField(upload_to='images')
    email=models.EmailField(max_length=50,unique=True)
    ph_no=models.CharField(max_length=20, blank=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

