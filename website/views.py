
from django.views.generic.list import ListView
from website.models import Image

class NewestView(ListView):

    context_object_name = 'images'
    model = Image
    queryset = Image.objects.all()
    template_name = 'list_of_images.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NewestView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['selected_page'] = 'newest'
        
        return context