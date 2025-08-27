from django.urls import path
from . import views

urlpatterns = [
    # イベント関連のURL
    path('', views.event_list, name='event_list'),
    path('list/', views.event_list_view, name='event_list_view'),
    path('create/', views.event_create, name='event_create'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/edit/', views.event_edit, name='event_edit'),
    path('<int:event_id>/delete/', views.event_confirm_delete, name='event_confirm_delete'),
    
    # ユーザー関連のURL
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/<int:user_id>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:user_id>/delete/', views.user_confirm_delete, name='user_confirm_delete'),
]