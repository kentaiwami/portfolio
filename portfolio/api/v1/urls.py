from rest_framework import routers
from .views import ContactViewSet


router = routers.DefaultRouter()
router.register(r'contact', ContactViewSet, base_name='add-contact')
