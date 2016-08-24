from django.conf.urls import url

from appBootstrap import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test/$', views.view_test, name='view_test'),
  url(r'^profile/$', views.profile, name='profile'),
]