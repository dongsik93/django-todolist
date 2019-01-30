from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    due_date = models.DateField()
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return self.content
        
        