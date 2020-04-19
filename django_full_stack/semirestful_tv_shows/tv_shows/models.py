from django.db import models

class Network(models.Model):
    name = models.CharField(max_length=20)

class Show(models.Model):
    title = models.CharField(max_length=65)
    network = models.ForeignKey(Network, related_name="shows", on_delete = models.CASCADE)
    release_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    desc = models.TextField()