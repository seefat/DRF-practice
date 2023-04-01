from django.urls import path 
from rest_framework.routers import DefaultRouter
from .views import StatusViewset

router = DefaultRouter()
router.register(r'status', StatusViewset, basename='status')
urlpatterns = []+router.urls
