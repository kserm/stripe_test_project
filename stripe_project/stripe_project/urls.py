from django.contrib import admin
from django.urls import path, include
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api'),
    path('', views.index),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('item/<int:id>', views.get_item, name='get-item'),
    path('buy/<int:id>', views.get_buy, name='buy-item'),
]
