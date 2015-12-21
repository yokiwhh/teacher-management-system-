#from django.conf.urls import patterns, url
from django.conf.urls.defaults import * 
from online import views
from django.conf.urls.static import static  
from django.conf import settings


urlpatterns = patterns('',
    #url(r'^$', views.login, name='login'),
    url(r'^$', views.home),
    url(r'^jianyue/$', views.jianyue),
    url(r'^superuserhahaha/$', views.superuser, name = 'manageer'),
    url(r'^superuseraddmajor/$', views.addmajor, name = 'add a major'),
    url(r'^superuseraddmessage/$', views.addmessage, name = 'add a message'),
    url(r'^superuseraddcollege/$', views.addcollege, name = 'add a college'),
    url(r'^login/$', views.login,name = 'login'),
    url(r'^messages/$', views.showmessage, name = 'show messages'),
    url(r'^college/[^/]+/$', views.collegeteachers, name = 'teachers in the college'),
    url(r'^deletemessage/?tid={{ m.teacher.teacherID }}&sid={{ m.student.studentID }}&date={{ m.date }}&time={{m.time }}/$', views.deletemessage, name = 'delete a massage'),
    url(r'^modifymessage/?tid={{ m.teacher.teacherID }}&sid={{ m.student.studentID }}&date={{ m.date }}&time={{m.time }}/$', views.modifymessage, name = 'modify a massage'),
    url(r'^regist/$', views.regist,name = 'regist'),
    url(r'^welcome/$', views.welcome,name = 'welcome'),
    url(r'^logout/$', views.logout,name = 'logout'),
    url(r'^search/$', views.search,name = 'search'),
    url(R'^teacherdetail/[^/]+/$', views.detail, name = 'detials'),
    url(r'^staticfiles/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIR, 'show_indexes': True}),
    url(r'^tuijian/$', views.tuijian, name = 'tuijian'),
    url(r'^error/$', views.error, name = 'error'),
)

#urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT ) 