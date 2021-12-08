from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username 

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish = models.DateField()
    genre = models.CharField(max_length=100)
    featured_by = models.CharField(max_length=100)
    user = models.ForeignKey('User', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Habit={self.name}>"

class BookRecord(models.Model):
    pass




    
    
