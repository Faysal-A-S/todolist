from django.db import models
from django.contrib.auth.models  import User
# Create your models here.

class Todo(models.Model):
    task = models.CharField( max_length=100)
    date = models.DateTimeField( auto_now=True)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'todo'

    def __str__(self):
        return self.task

    
   