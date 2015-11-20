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