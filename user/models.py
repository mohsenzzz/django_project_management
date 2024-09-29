from audioop import reverse

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator,MaxValueValidator
from sqlparse.engine.grouping import group

from group.models import Group


# Create your models here.

class User(AbstractUser):
    email_active_code = models.CharField(max_length=100, unique=True,null=True,blank=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,null=True,related_name='user_groups')
    profile = models.ImageField(upload_to='profile',blank=True,null=True)
    class Meta:
        db_table = 'user'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('user_profile', slug=[self.id])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(User, self).save(*args, **kwargs)