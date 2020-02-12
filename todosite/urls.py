from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()
from todo import views
from django.views.generic.base import TemplateView

urlpatterns = patterns('',

   url(r'^admin/', include(admin.site.urls)),#admin app
   # API authentication
   url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

   url(r'^register/$', views.RegistrationView.as_view()), #registration endpoint
   url(r'^umodel/$', views.UserModelView.as_view()), #user model endpoint
   url(r'^signup/$', views.signup, name='signup'), #registration form
   url(r'^accounts/', include('django.contrib.auth.urls')),  # login loogut urls
   url('', TemplateView.as_view(template_name='home.html'), name='home'),  # to home

   )
