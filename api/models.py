from django.db import models
from django.contrib.auth.models import AbstractUser
from project import settings

class User(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>" 


class Genre(models.Model):
    genre =models.CharField(max_length=100)

    def __str__(self):
        return self.genre

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication_date = models.DateField()
    publisher =models.CharField(max_length=100, blank=True, null=True)
    genre = models.ManyToManyField(to=Genre, related_name="books", blank=True)
    featured = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name="books", blank=True,  on_delete=models.CASCADE)

    class Meta:
        ordering= ['title']
        unique_together = ['title', 'author']


    def __str__(self):
        return self.title





    
    
