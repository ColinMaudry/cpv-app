from django.db import models

# Create your models here.
class Code(models.Model):
    id = models.CharField(max_length = 10, primary_key=True)
    name = models.CharField(max_length=512)
    parent = models.ForeignKey('self', models.SET_NULL, blank=True, null=True)



