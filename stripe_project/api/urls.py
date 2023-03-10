from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register('item', views.ItemViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls)), 
]
