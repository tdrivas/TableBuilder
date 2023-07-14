from django.db import models

# Create your models here.

class DynamicTable(models.Model):
    field_type = models.CharField(max_length=100)
    field_title = models.CharField(max_length=100)