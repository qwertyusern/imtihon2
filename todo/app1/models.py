from django.db import models

class Todo(models.Model):
    sarlavha=models.CharField(max_length=120)
    vaqti=models.DateTimeField()
    malumot=models.TextField()
    status=models.BooleanField()
    def __str__(self):
        return self.sarlavha
