from django.conf.urls import patterns, include, url
from website.models import Image
from django.views.generic.detail import DetailView
from website.views import NewestView, BestView, UploadView, RegisterView,\
    LoginView, VoteUpView, VoteDownView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

urlpatterns = patterns('',
    # Examples:
    #url(r'^(?P<pk>\d+)/$', DetailView.as_view(
    #                                        template_name='details.html',
    #                                        #queryset=Image.objects.filter(pk=1)
    #                                        model=Image
    #                                         )
    #    ),
    url(r'^img/(?P<slug>[-a-zA-Z0-9]+)/$', DetailView.as_view(
                                            template_name='details.html',
                                            context_object_name='image',
                                            model=Image
                                             )
        ),
    url(r'^img/(?P<slug>[-a-zA-Z0-9]+)/\+/$', VoteUpView.as_view(                                             )
        ),
    url(r'^img/(?P<slug>[-a-zA-Z0-9]+)/\-/$', VoteDownView.as_view(                                             )
        ),
    url(r'^$', NewestView.as_view()),
    #url(r'^search/', SearchView.as_view()),
    url(r'^search/', 'website.views.search'),
    url(r'^best/$', BestView.as_view()),
    url(r'^upload/$', UploadView.as_view()),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^registered/$', TemplateView.as_view(template_name='registered.html',)),
    url(r'^login/$', LoginView.as_view()),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    
)
