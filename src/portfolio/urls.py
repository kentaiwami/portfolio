from django.conf.urls import url
from . import views

app_name = 'portfolio'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<e_product_id>[0-9]+)/$', views.engineer_work_detail, name='engineer_work_detail'),
    url(r'^all_photographer_works/', views.all_photographer_works, name='all_photographer_works'),
    url(r'^post_comment/', views.post_comment, name='post_comment'),
    url(r'^post_contact/', views.post_contact, name='post_contact'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^thanks/', views.thanks, name='thanks'),
    url(r'^(?P<e_product_id>[0-9]+)/pp$', views.privacy_policy, name='privacy_policy')
    # url(r'^engineer_works_all', views.engineer_works_all, name='engineer_works_all'),
]
# handler404 = 'views.handler404'
# handler500 = 'views.handler500'
# handler403 = 'views.handler403'
# handler400 = 'views.handler400'
