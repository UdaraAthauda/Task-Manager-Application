from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    postDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, max_length=20, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):

    reviewerName = models.CharField(max_length=50)
    reviewTitle = models.CharField(max_length=50)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.task} - {self.reviewTitle}"