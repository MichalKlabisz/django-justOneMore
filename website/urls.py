from django.conf.urls import patterns, include, url
from website.models import Image
from django.views.generic.detail import DetailView
from website.views import NewestView, Top100View, UploadView

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
    url(r'^img/(?P<slug>[-a-zA-Z0-9]+)/$', DetailView.as_view(
                                            template_name='details.html',
                                            model=Image
                                             )
        ),
    url(r'^$', NewestView.as_view()),
    url(r'^top100/$', Top100View.as_view()),
    url(r'^upload/$', UploadView.as_view()),
    #url(r'^login/$', LoginView.as_view()),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    
)
