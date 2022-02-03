from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import  date
import datetime

# Create your models here.

class Blog(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    overview = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to= 'thumbnails/', null=True, blank=True)
    featured = models.BooleanField(default=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    comment_counts = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def get_label(self):
        if self.created.date() > date.today() - datetime.timedelta(days=4):
           return True 
        else:
           return False

    @property
    def getCommentCount(self):
        comments = self.comment_set.all()
        totalComments = comments.count()
        self.comment_counts = totalComments
        self.save()
    class Meta:
        ordering = [
            '-featured', '-created'
        ]




class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    def __str__(self):
        return self.name



    
class Comment(models.Model):
    user_name =  models.CharField(max_length=50)
    email = models.EmailField(max_length=200, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user_name)


class Contact(models.Model):
    user_name =  models.CharField(max_length=50)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=300, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return str(self.user_name)
    



class About(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    email = models.CharField( max_length=50, null=True, blank=True)
    telephone = models.CharField( max_length=10 ,null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    social_fb = models.CharField(max_length=300, null=True, blank=True)
    social_yt = models.CharField(max_length=300, null=True, blank=True)
    social_github = models.CharField(max_length=300, null=True, blank=True)
    social_linkedin = models.CharField(max_length=300, null=True, blank=True)
    social_twitter = models.CharField(max_length=300, null=True, blank=True)
    social_insta = models.CharField(max_length=300, null=True, blank=True)
    
    


    def __str__(self):
        return self.name
    
    