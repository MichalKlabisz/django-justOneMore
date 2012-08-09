
from django.views.generic.list import ListView
from website.models import Image
from django.views.generic.edit import CreateView, FormView
from website.forms import UploadForm, SearchForm
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect


def_pagination = 10

class NewestView(ListView):
    queryset = Image.objects.all().order_by('-pub_date')
    template_name = 'list_of_images.html'
    paginate_by = def_pagination

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NewestView, self).get_context_data(**kwargs)
        context['selected_page'] = 'newest'
        
        return context
    
class SearchView(FormView):
    template_name = 'list_of_images.html'
    form_class = SearchForm
    paginate_by = def_pagination
    success_url = '/search/'
    def get_query_set(self):
        
    
        if self.request.method == 'POST': # If the form has been submitted...
            form = SearchForm(self.request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
                return Image.objects.all()
                return Image.objects.filter(title__icontains = form.cleaned_data['search_field'])
        # def get_query_set(self):
        #    return super(MaleManager, self).get_query_set().filter(sex='M')
        return Image.objects.all()


    #return Image.objects.filter(title__icontains = self.REQUEST['search_field'])
    
class Top100View(ListView):
    queryset = Image.objects.all().order_by('title')
    template_name = 'list_of_images.html'
    paginate_by = def_pagination

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Top100View, self).get_context_data(**kwargs)
        context['selected_page'] = 'top100'
        
        return context
    
class DetailsView(DetailView):
    queryset = Image.objects.all().order_by('-pub_date')
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NewestView, self).get_context_data(**kwargs)
        context['selected_page'] = 'newest'
        
        return context
    
class UploadView(CreateView):
    template_name = 'upload.html'
    form_class = UploadForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        context['selected_page'] = 'upload'
        
        return context
    
    def form_valid(self, form):
        img = form.save(commit=False)
        img.sent_by = self.request.user
        img.save()    
        form.save_m2m()    
        self.object = img
        return HttpResponseRedirect(self.get_success_url())
    
class LoginView(FormView):
    template_name = 'login.html'
    #form_class = LoginForm
    form_class = AuthenticationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['selected_page'] = 'login'
        
        return context
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/registered/'