from django.db import models
from django.contrib.auth.models import User
import re

# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email_input']):
            errors['email'] = 'Please enter a valid email address'
        elif User.objects.filter(email=postData['email_input']).exists():
            errors['emailunique'] = "Email already registered, please login."
        if len(postData['password_input']) < 5:
             errors['password'] = 'please have a password greater than 5 Charaters'
        if postData['confirmpw_input'] != postData['password_input']:
            errors['confirm_pw'] = "Your password and what you typed in comfirm pw dont match try agian"
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email_input']):
            errors['email'] = 'Please enter a valid Email address!'
        if len(postData['password_input']) < 5:
            errors['password'] = 'Please enter an email that contains 5 or more character'
        return errors



class User(models. Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Comments(models. Model): 
    comment = models.CharField(max_length=255, null=True)
    user_posted = models.ForeignKey(User, related_name="poster", on_delete = models.CASCADE)
    user_comment = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)








