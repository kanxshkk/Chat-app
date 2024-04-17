from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)
=======
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=200)
>>>>>>> 3484baaddb60d1adf35712eb69ed156742d37cec

    def __str__(self):
        return self.name

<<<<<<< HEAD

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
=======
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
>>>>>>> 3484baaddb60d1adf35712eb69ed156742d37cec
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
<<<<<<< HEAD
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


=======
        ordering = ['-updated','-created']

    def __str__(self):
        return str(self.name)
    
>>>>>>> 3484baaddb60d1adf35712eb69ed156742d37cec
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
=======
    
    class Meta:
        ordering = ['-updated','-created']
        
    def __str__(self):
        return self.body[:50]
>>>>>>> 3484baaddb60d1adf35712eb69ed156742d37cec
