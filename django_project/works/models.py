from django.db import models


class Metadata(models.Model):
    title = models.TextField()
    contributors = models.TextField()
    ISWC = models.TextField()

    def __str__(self):
        return f"{self.ISWC}: <<{self.title}>> by {self.contributors}"
