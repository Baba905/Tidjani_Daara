from django.db import models
from Daara.summarize import summarization

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=100)
    upload = models.FileField(upload_to='uploads/document')
    upload_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='uploads/covers', null=True, blank=True)
    summary = models.TextField(null=True, blank=True)


    def delete(self, *args, **kwargs):
        self.upload.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
    
    def summarization(self):
        if self.summary==None:
            self.summary = summarization(self.upload.path)
            self.save()