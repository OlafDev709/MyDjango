from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"
        ordering = ['completed', 'title']