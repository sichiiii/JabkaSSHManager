from django.db import models

class SSHConnection(models.Model):
    name = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    port = models.IntegerField(default=22)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
