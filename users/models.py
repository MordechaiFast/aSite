from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    content = models.TextField()