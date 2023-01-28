from django.db import models


class Blog(models.Model):
    title = models.TextField(max_length=200)
    date = models.DateField()
    text_blog = models.TextField(max_length=5000)

    def __str__(self):
        return self.title
