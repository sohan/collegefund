from django.db import models
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField
from django.utils.encoding import smart_str

class Student(models.Model):
    name = models.CharField(max_length=200)
    university = models.CharField(max_length=500)
    #photo = models.ImageField(upload_to='photos')
    track_record = ListField(EmbeddedModelField('Achievement'))

    def __str__(self):
        return smart_str('%s' % self.name)
    
class Achievement(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField()
    date_end = models.DateField(null=True)
    title = models.CharField(max_length=500)
    text = models.TextField()

    def __str__(self):
        return smart_str('%s | %s...' % (self.title, self.text[:20]))
