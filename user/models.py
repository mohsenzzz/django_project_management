from audioop import reverse

from django.db import models
from django.utils.text import slugify
from sqlparse.engine.grouping import group

from group.models import Group


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    family= models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.family}'

    def get_absolute_url(self):
        return reverse('user_profile', slug=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(User, self).save(*args, **kwargs)