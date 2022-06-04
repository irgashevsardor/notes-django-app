from django.db import models


class Topic(models.Model):
    topic_theme = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic_theme


class Entry(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.text) < 50:
            return self.text
        else:
            return f"{self.text[:50]}..."

    class Meta:
        verbose_name_plural = 'entries'
