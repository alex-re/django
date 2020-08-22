from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # `auto_now=True` means update time after each update but `auto_now_add=True` means time tht its added.
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # `on_delete` means what we whant to do if user deleted (in this case we delete posts if user deleted but if the post deleted user will not delete!) (if we want to delete post or keep it with none author or ...)

    def __str__(self):
        return self.title