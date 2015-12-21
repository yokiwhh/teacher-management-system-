<<<<<<< HEAD
#from django.conf.urls import patterns, url
from django.conf.urls.defaults import * 
from online import views
from django.conf.urls.static import static  
from django.conf import settings


urlpatterns = patterns('',
    #url(r'^$', views.login, name='login'),
    url(r'^$', views.home),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
    url(r'^staticfiles/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS, 'show_indexes': True}),
)

#urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT ) 
=======
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onlineproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^online/', include('online.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
>>>>>>> 9f023d7cbe350bd2a4c39eeee844c5839d636faf
