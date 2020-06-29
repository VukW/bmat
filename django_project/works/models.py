from django.db import models


class Contributor(models.Model):
    name = models.CharField(max_length=128, unique=True, db_index=True)

    def __str__(self):
        return str(self.name)


class Metadata(models.Model):
    title = models.CharField(max_length=128, db_index=True)
    contributors = models.ManyToManyField(Contributor)
    ISWC = models.CharField(max_length=12, unique=True, null=True, db_index=True)

    def __str__(self):
        return f"{self.ISWC}: <<{self.title}>> by {self.contributors}"
