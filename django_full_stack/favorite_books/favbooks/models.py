from django.db import models
import re

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
    password = models.TextField()
    objects = Manager()

class bookCheck(models.Manager):
    def book_validator(self,postData):
        errors = {}
        if len(postData['title']) < 0:
            errors['title_len'] = "Title is required."
        if len(postData['desc']) < 5:
            errors['desc_len'] = "Book description should be at least 5 characters."
        return errors

class book(models.Model):
    title = models.CharField(max_length=65)
    desc = models.TextField()
    posted_by = models.ForeignKey(User, related_name="books", on_delete = models.CASCADE)
    objects = bookCheck()

class Like(models.Model):
    liked_by = models.ForeignKey(User, related_name="user_likes", on_delete = models.CASCADE)
    book_liked = models.ForeignKey(book, related_name="message_likes", on_delete = models.CASCADE, default=0)
