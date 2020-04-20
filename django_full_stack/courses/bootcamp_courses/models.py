from django.db import models

class coursemanager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name must be at least 5 characters."
        if len(postData['description']) < 15:
            errors["description"] = "Description must be at least 15 characters."
        return errors

class Description(models.Model): 
    text = models.CharField(max_length = 255) 

class Course(models.Model): 
    name = models.CharField(max_length = 100)
    description = models.OneToOneField(Description,on_delete = models.CASCADE, primary_key = True) 
    date_added = models.DateTimeField(auto_now_add=True)
    objects = coursemanager()