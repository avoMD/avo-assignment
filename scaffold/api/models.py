from django.db import models


class Seed(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    class Meta:
        db_table = "seed"
