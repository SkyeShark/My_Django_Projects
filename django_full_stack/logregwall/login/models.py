from django.db import models
import datetime, re

class Manager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name_len'] = "First name should be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name_len'] = "Last name should be at least 2 characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = ("Invalid email address!")
        if User.objects.filter(email=postData['email']).exists():
            errors['emailunique'] = "Email already registered, please login."
        if postData['password'] != postData['confirmpw']:
            errors['pwmatch'] = "Passwords must match."
        if len(postData['password']) < 8:
            errors['pwlen'] = "Password should be at least 8 characters."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=70)
    passhashed = models.TextField()
    objects = Manager()

class Post(models.Model):
    message = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User, related_name='user_messages', on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')
    objects = models.Manager()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="post_comments", on_delete=models.CASCADE)
    objects = models.Manager()