from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.addcourse),
    url(r'^show_delete$', views.showdelete),
    url(r'^remove_course$', views.delcourse)
  ]