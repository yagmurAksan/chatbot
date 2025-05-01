from django.db import models

class Conversation(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    classification_result = models.CharField(max_length=255, null=True, blank=True)  # Sınıflandırma sonucu

    def __str__(self):
        return f"Conversation {self.id}"
