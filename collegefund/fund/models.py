from django.db import models
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField
from django.utils.encoding import smart_str

class Student(models.Model):
    name = models.CharField(max_length=200)
    university = models.CharField(max_length=500)
    #photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return smart_str('%s' % self.name)
    
class Achievement(models.Model):
    student = models.ForeignKey('Student')
    summary = models.TextField()

    def __str__(self):
        return smart_str('%s: %s' % (self.student.name, str(self.summary)[:20]))
