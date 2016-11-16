from __future__ import unicode_literals

from django.db import models
import jsonfield

#models

class Photo(models.Model):
    url_photo = models.CharField(max_length=600, blank=True)
    key = models.CharField(max_length=300)
    last_modified = models.DateTimeField()
    etag= models.CharField(max_length=300)
    size = models.IntegerField()
    storage_class = models.CharField(max_length=100)
    exif_keys = jsonfield.JSONField
    



