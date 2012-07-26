
from django.views.generic.list import ListView
from website.models import Image

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
    
class Top100View(ListView):
    queryset = Image.objects.all().order_by('title')
    template_name = 'list_of_images.html'
    paginate_by = def_pagination

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Top100View, self).get_context_data(**kwargs)
        context['selected_page'] = 'top100'
        
        return context