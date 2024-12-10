from django.db import models

class ConfigurationFile(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title