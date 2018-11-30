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
    path('groceries/purchaser/', views.user_purchaser_list, name='user_purchaser_list'),

    # 127.0.0.80000/groceries/bought_list -->
    path('groceries/<bought_date>/bought_list/', views.bought_date_list, name='bought_date_list'),

    # 127.0.0.8000/groceries/<int:pk>/edit_item/ --> local
    path('groceries/<int:pk>/edit_item/', views.edit_item, name='edit_item'),

    # 127.0.0.80000/groceries/<int:pk>/delete_grocery/ -->
    path('groceries/<int:pk>/delete', views.delete_item, name='delete_item'),

]