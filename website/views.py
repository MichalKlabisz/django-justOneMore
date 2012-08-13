from django.db.models import Q
from django.views.generic.list import ListView
from website.models import Image
from django.views.generic.edit import CreateView, FormView, FormMixin
from website.forms import UploadForm, SearchForm
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext, Context
import operator


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
    
#class SearchView(ListView):
#    template_name = 'list_of_images.html'
    #form_class = SearchForm
#    paginate_by = def_pagination
    #success_url = '/search/'
#    context_object_name = 'page_obj'
#    queryset = Image.objects.all()
    
    #def get_queryset(self):
    #    return Image.objects.all()
    
        #if self.request.method == 'POST': # If the form has been submitted...
        #    form = SearchForm(self.request.POST) # A form bound to the POST data
        #    if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
       #         return Image.objects.all()
        #        return Image.objects.filter(title__icontains = form.cleaned_data['search_field'])
        #return Image.objects.all()


    #return Image.objects.filter(title__icontains = self.REQUEST['search_field'])

def search(request):

    if request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            #Based on http://stackoverflow.com/questions/1957240/filter-using-q-object-with-dynamic-from-user/1957263#1957263
            queryset = form.cleaned_data['search_field'].split()
            query = reduce(operator.or_, ((Q(title__icontains = x) | Q(description__icontains = x)) for x in queryset))
            #results = Image.objects.filter(Q(title__iexact = query) | Q(description__icontains = query))
            results = Image.objects.filter(query)
        else:
            results = []
    else:
        form = SearchForm()
        results = []
    
    #results = Image.objects.all()


    return render_to_response(
        'search.html',
        RequestContext(request, {
            'form': form,
            'search_results': results,
        })
    )
    
class BestView(ListView):
    queryset = Image.objects.all().order_by('-points')
    template_name = 'list_of_images.html'
    paginate_by = def_pagination

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BestView, self).get_context_data(**kwargs)
        context['selected_page'] = 'best'
        
        return context
    
class VoteUpView(DetailView):
    model = Image
    context_object_name='image'
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(VoteUpView, self).get_context_data(**kwargs)
        
        return context
    
    #def get_object(self, queryset=None):
    #    img = super(VoteUpView, self).get_object()
    #    context = self.context
    #    if context['voteUp'] == True:
    #        img.points += 1
    #    else:
    #        img.points -= 1
        #img.save()
    #    return img
    
    def get_object(self, queryset=None):
        img = super(VoteUpView, self).get_object()
        img.points += 1
        img.save()
        
        return img
    

class VoteDownView(VoteUpView):
    def get_object(self, queryset=None):
        img = super(VoteUpView, self).get_object()
        img.points -= 1
        img.save()
        
        return img
    
#class VoteView(DetailView):
    
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