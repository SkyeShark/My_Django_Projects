from django.db import models
import datetime

class showmanager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters."
        if len(postData['network']) < 3:
            errors["network"] = "Network name should be at least 3 characters."
        if postData['reldate'] is '':
            release = datetime.datetime.now() 
            errors["reldate"] = "Release date must be entered."
        else:
            release = datetime.datetime.strptime(postData['reldate'], '%Y-%m-%d')
        if release > datetime.datetime.now():
            errors["reldate"] = "Release date cannot be in the future."
        if len(postData['description']) < 10:
                if len(postData['description']) > 0:
                    errors["description"] = "Description should be at least 10 characters."
                else:
                    pass
        return errors

class Network(models.Model):
    name = models.CharField(max_length=20)

class Show(models.Model):
    title = models.CharField(max_length=65)
    network = models.ForeignKey(Network, related_name="shows", on_delete = models.CASCADE)
    release_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    desc = models.TextField()
    objects = showmanager()