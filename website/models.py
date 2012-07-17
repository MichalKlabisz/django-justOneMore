from django.db import models
from django.template.defaultfilters import slugify
from django.utils.datetime_safe import datetime

class Image(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    description = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/%Y-%m-%d')
    
    def __unicode__(self):
        return self.title
    
    def save(self):
        self.slug = slugify(self.title)
        self.pub_date = datetime.now()
        super(Image, self).save()
