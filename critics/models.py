from django.db import models
from django.contrib.auth.models import User
class Critic(models.Model):
    title = models.CharField(max_lenght=255)
    movie_name = models.CharField(max_lenght=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
