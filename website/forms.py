from django.forms.models import ModelForm
from website.models import Image

class UploadForm(ModelForm):
    class Meta:
        model = Image
        exclude = ('pub_date', 'slug')
    
    def handle_uploaded_file(self, f):
        with open(f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)