from django.db import models

from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='media/profile_pics/default.png', upload_to='media/profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kawrgs):  # we are aboute creating our own save method and it has to get sth from its parrents.
        super().save(*args, **kawrgs)  # this super hints to main save() method.

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
