from django.db import models
from django.contrib.auth.models import User
    
class Post(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post/',default='default.jpg')
    content=models.TextField()
    createdDate=models.DateField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    public=models.BooleanField(default=True)