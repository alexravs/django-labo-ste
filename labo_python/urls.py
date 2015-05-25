from django.conf.urls import patterns, include, url
from django.contrib import admin
from labo_python import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'labo_python.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url("^labo_python/$", views.base ),
    url("^labo_python/login", views.login ),
    url("^labo_python/sign_up$", views.sign_up ),
    url("^labo_python/sign_up_done", views.sign_up_done ),
    url("^labo_python/sign_in_done", views.log_in_done ),
    url("^labo_python/log_out", views.log_out ),
    
)
