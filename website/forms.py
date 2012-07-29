from django.forms.models import ModelForm
from website.models import Image
from django.contrib.auth.models import User

class UploadForm(ModelForm):
    class Meta:
        model = Image
        exclude = ('pub_date', 'slug')
    
    def handle_uploaded_file(self, f):
        with open(f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
                
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')