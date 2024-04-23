from email.policy import default
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# always remember to makemigrations when modifying the models and migrate them afterwards.
# creating a category model for our posts.
class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Getting the absolute url path, in this case for the redirect when post is created from the browser.
    def get_absolute_url(self):
        #return reverse ('article', args=(str(self.id)))
        return reverse ('home')

# The post model for adding our blog data to the db
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length=255, default="First Posts")

    # for the author and the title they created. displayed at the botom of the view when a blog is in view.
    def __str__(self):
        return self.title + "  |  " + str(self.author) # remember to pass in the author object as a string


    # Getting the absolute url path, in this case for the redirect when post is created from the browser.
    def get_absolute_url(self):
        #return reverse ('article', args=(str(self.id)))
        return reverse ('home')











