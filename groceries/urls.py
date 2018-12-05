from django.urls import path, include
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

    # 127.0.0.80000/groceries/<int:pk>/delete_grocery/ --> local
    path('groceries/<int:pk>/delete', views.delete_item, name='delete_item'),

    # 127.0.0.80000/groceries/piggy_top_up/ -->
    path('groceries/piggy_top_up/', views.piggy_top_up, name='piggy_top_up'),

    # 127.0.0.80000/groceries/Piggy_top_up_list/ --> local
    path('groceries/piggy_top_up_list/', views.piggy_top_up_list, name='piggy_top_up_list'),

    # 127.0.0.80000/groceries/<int:pk>/edit_item/ --> local
    path('groceries/<int:pk>/edit_reason', views.edit_reason, name='edit_reason'),

    # 127.0.0.80000/groceries/<int:pk>/delete_reason/ --> local
    path('groceries/<int:pk>/delete_reason', views.delete_reason, name='delete_reason'),
]