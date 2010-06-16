from django.conf.urls.defaults import *
from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       (r'^view_status/$' , view_status),
                       (r'^update_status/$' , update_status),
                       (r'^swapper/$' , swapper),
                       (r'^$' , tweet_pipe),
                        
    # Example:
    # (r'^twitter_pipe/', include('twitter_pipe.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
