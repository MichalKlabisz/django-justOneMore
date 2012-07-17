from models import Image
from django.contrib import admin

class ImageAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('title',) }

admin.site.register(Image, ImageAdmin)