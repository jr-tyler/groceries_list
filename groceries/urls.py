from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.80000
    path('', views.grocery_list, name='grocery_list'),

    # 127.0.0.80000/groceries/new --> local
    path('groceries/new/', views.groceries_new, name='groceries_new'),

    # 127.0.0.80000/groceries/piggy --> local
    path('groceries/piggy/', views.piggy_page, name='piggy_page'),

    # 127.0.0.80000/groceries/<int> --> local
    path('groceries/<int:person_id>/', views.purchaser_list, name='purchaser_list'),

# 127.0.0.80000/groceries/purchaser --> local
    path('groceries/purchaser/', views.user_purchaser_list, name='user_purchaser_list')
]