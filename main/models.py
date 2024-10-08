from django.db import models
from django.db.models import TextField, EmailField
class PreviewImage(models.Model):
    image = models.ImageField(upload_to='images')
    description = models.TextField()

    def __str__(self) -> TextField:
        return self.description

class Contact(models.Model):
    number = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self) -> EmailField:
        return self.email
