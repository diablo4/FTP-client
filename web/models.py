from django.db import models


class UploadFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True)

class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
