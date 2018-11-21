from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.80000
    path('', views.grocery_list, name='grocery_list'),
]