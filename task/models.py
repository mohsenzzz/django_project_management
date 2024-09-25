from audioop import reverse
from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.db import models
from user.models import User
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=600)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    asigned_to = models.ManyToManyField(User,related_name='asigned')
    expire_time = models.DateTimeField(default=datetime.now() + relativedelta(year=1),
                                       null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', slug=[self.id])
