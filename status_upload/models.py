from django.db import models


class OperationTypeModel(models.Model):
    name_of_type = models.CharField(max_length=100)

