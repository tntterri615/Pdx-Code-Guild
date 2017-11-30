from django.db import models


class TinyUrl (models.Model):
    code = models.CharField(max_length=20),
    url = models.CharField(max_length=400)

    def __str__(self):
        return self.code




