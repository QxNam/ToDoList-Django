from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'App_task'