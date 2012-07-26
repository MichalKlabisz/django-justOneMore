from django.conf.urls import patterns, include, url
from django.views.generic.list import ListView
from website.models import Image
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from website.views import NewestView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myBlogExample.views.home', name='home'),
    # url(r'^myBlogExample/', include('myBlogExample.foo.urls')),
    #url(r'^add/', 'website.views.upload_file'), 
    #url(r'^(?P<pk>\d+)/$', DetailView.as_view(
    #                                        template_name='detail.html',
    #                                        #queryset=Image.objects.filter(pk=1)
    #                                        model=Image
    #                                         )
    #    ),
    #url(r'^(?P<slug>[-a-zA-Z0-9]+)/$', DetailView.as_view(
    #                                        template_name='detail.html',
    #                                        model=Image
    #                                         )
    #    )
    url(r'^$', NewestView.as_view()
        ),
    
)
