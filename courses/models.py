from django.db import models
from django.contrib import admin


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    studentslist = models.TextField(blank=True)


    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    grad_year = models.CharField(max_length=100, blank=True)
    major = models.CharField(max_length=100, blank=True)
    minor = models.CharField(max_length=100, blank=True)
    interests = models.TextField(blank=True)
    class_list = models.TextField(blank=True)

    def __str__(self):
        return self.name
