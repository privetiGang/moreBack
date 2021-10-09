from django.db import models


class Dict(models.Model):
    key = models.TextField()
    value = models.TextField()


class MetaFields(models.Model):
    name = models.TextField()
    dates = models.TextField()
    fields = models.TextField()
    description = models.TextField()
    size = models.TextField()
    completenes = models.IntegerField()


class Mts(models.Model):
    contacts = models.TextField()
    sum = models.IntegerField()
    date = models.DateField()
    metafields = models.ForeignKey(MetaFields, on_delete=models.CASCADE)

class Magazine(models.Model):
    fio = models.TextField()
    phone_number = models.TextField()
    address = models.TextField()
    metafields = models.ForeignKey(MetaFields, on_delete=models.CASCADE)

class Adidas(models.Model):
    contacts = models.TextField()
    sum = models.IntegerField()
    date = models.DateField()
    sex = models.TextField()
    age = models.IntegerField()
    metafields = models.ForeignKey(MetaFields, on_delete=models.CASCADE)

class TypeDataSet(models.Model):
    adidas = models.ForeignKey(Adidas, on_delete=models.CASCADE)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    mts = models.ForeignKey(Mts, on_delete=models.CASCADE)
    type = models.IntegerField()
