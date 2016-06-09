from django.conf.urls import url
from . import views

# Here is the setup for the urls of the web application
# The app name is used as a url namespace
app_name = 'schools'
# Here are the url patterns and the views they correspond to
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^member/(?P<member_id>[0-9]+)/$', views.memberDetail, name='memberDetail'),
    url(r'^school/(?P<school_id>[0-9]+)/$', views.schoolDetail, name='schoolDetail'),
    url(r'^addMember/$', views.addMember, name='addMember'),
    url(r'^addSchool/$', views.addSchool, name='addSchool'),
]