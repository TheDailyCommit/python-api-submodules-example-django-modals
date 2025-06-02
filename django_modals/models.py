from django.db import models
from django.utils import timezone


class Todo(models.Model):
    """
    A simple todo list model that can be shared across different projects.
    """

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.title
