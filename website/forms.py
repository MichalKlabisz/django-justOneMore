from django.forms.models import ModelForm
from website.models import Image
from django.contrib.auth.models import User
from django import forms


class UploadForm(ModelForm):
    class Meta:
        model = Image
        exclude = ('pub_date', 'slug', 'sent_by')
    
    #def handle_uploaded_file(self, f):
    #    with open(f.name, 'wb+') as destination:
    #        for chunk in f.chunks():
    #            destination.write(chunk)
                
#class LoginForm(ModelForm):
#    class Meta:
#        model = User
#        fields = ('username', 'password')
        
class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=50)