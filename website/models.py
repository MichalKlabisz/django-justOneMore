from django.db import models
from django.template.defaultfilters import slugify
from django.utils.datetime_safe import datetime
from django.contrib.auth.models import User

class Image(models.Model):
    title = models.CharField(max_length=50, unique=True)
    pub_date = models.DateTimeField()
    description = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    sent_by = models.ForeignKey(User, editable=False, related_name='user_sent_by')
    points = models.IntegerField(editable=False, default=0)
    who_voted = models.ManyToManyField(User, editable=False, related_name='user_who_voted')
    image = models.ImageField(upload_to='images/%Y-%m-%d')
    
    def __unicode__(self):
        return self.title
    
    def save(self):
        self.slug = slugify(self.title)
        if not self.pub_date:
            self.pub_date = datetime.now()
        
        super(Image, self).save()
