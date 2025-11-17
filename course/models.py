from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    phone = models.CharField(max_length=20, blank=True , null=True)

    def __str__(self):
        return self.user.username
    


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(unique=True)
    # instructor = models.ForeignKey(InstructorUser, on_delete=models.CASCADE,related_name='courses')
    Student = models.ManyToManyField(Student,related_name='courses')

    def __str__(self):
        return self.title

