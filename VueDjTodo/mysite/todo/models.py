from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField('NAME', max_length=5, blank=True)
    todo = models.CharField('TODO', max_length=50)
    
    def __str__(self):
        return self.name + ": "+ self.todo

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.name:
            self.name = 'devKya'
        super().save()