from django.db import models


class Dict(models.Model):
    key = models.TextField()
    value = models.TextField()
