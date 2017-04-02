from django.conf.urls import url

from . import views

app_name = 'portfolio'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<e_product_id>[0-9]+)/$', views.engineer_work_detail, name='engineer_work_detail'),
    url(r'^photographer_all/', views.photographer_all, name='photographer_all'),
    url(r'^get_comment/', views.get_comment, name='get_comment'),
    url(r'^thanks/', views.thanks, name='thanks'),
    # url(r'^engineer_works_all', views.engineer_works_all, name='engineer_works_all'),
]
handler404 = 'views.handler404'
handler500 = 'views.handler500'
handler403 = 'views.handler403'
handler400 = 'views.handler400'
