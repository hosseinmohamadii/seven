from django.db import models
from django.contrib.auth.models import User
class Critic(models.Model):
    title = models.CharField(max_length=200)
    movie_name = models.CharField(max_lenght=150)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
