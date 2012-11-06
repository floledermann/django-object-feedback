from django.conf.urls.defaults import patterns, url

from feedback import views

urlpatterns = patterns('',
    url(r'^send/$', views.send_feedback, name='feedback_send'),
)



