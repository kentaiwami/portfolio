from django.conf.urls import url

from . import views

app_name = 'portfolio'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>[0-9]+)/$', views.engineer_work_detail, name='engineer_work_detail'),
]
