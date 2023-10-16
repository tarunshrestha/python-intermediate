from django.db import models


# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    course = models.CharField(max_length=50)  # To change 1: python manage.py makemigrations / 2:python manage.py migrate
