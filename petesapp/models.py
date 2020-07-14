from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname_input']) < 2:
            errors ['first_name'] = "Please enter a valid first name"
        if len(postData['lname_input']) < 2:
            errors ['last_name'] = "Please enter a valid last name"
        if not EMAIL_REGEX.match(postData['email_input']):
            errors['email'] = 'Please enter a valid email address'
        if User.objects.filter(email=postData['email']).exists():
            errors['emailunique'] = "Email already registered, please login."
        if len(postData['password_input']) < 5:
             errors['password'] = 'please have a password greater than 5 Charaters'
        if postData['confirmpw_input'] != postData['password_input']:
            errors['confirm_pw'] = "Your password and what you typed in comfirm pw dont match try agian"
        if len(postData['workout_input']) < 20:
            errors['workout_goals'] = "Tell us more why your working out."
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email_input']):
            errors['email'] = 'Please enter a valid Email address!'
        if len(postData['password_input']) < 5:
             errors['password'] = 'Please enter an email that contains 5 or more character'
        if postData['confirmpw_input'] != postData['password_input']:
            errors['confirm_pw'] = "Your password and what you typed in comfirm pw dont match try agian"
        return errors



class User(models. Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    workout_goals = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Comments(models. Model):
    user_comment = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Video(models. Model):
    likes = models.ManyToManyField(User, related_name="user_likes")
    vid_comment= models.ForeignKey(User, related_name="vid_comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)




