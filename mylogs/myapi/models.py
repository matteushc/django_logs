from django.db import models

class Logs(models.Model):
    name_app = models.CharField(max_length=60)
    data = models.CharField(max_length=60)
    message = models.CharField(max_length=60)
    type_message = models.CharField(max_length=60)
    def __str__(self):
        return self.name_app