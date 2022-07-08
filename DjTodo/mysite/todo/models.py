from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField('NAME', max_length=5, blank=True)
    todo = models.CharField('TODO', max_length=50)
    
    def __str__(self):
        return self.todo
    
    def save(self):
        if not self.name:
            self.name = "devKya"
        super().save()