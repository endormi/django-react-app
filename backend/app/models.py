from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=25)
    paradigm = models.CharField(max_length=125)
    created_by = models.CharField(max_length=50)


class Faangm(models.Model):
    name = models.CharField(max_length=25)
    created = models.CharField(max_length=4)
    location = models.CharField(max_length=50)
