from django.urls import path
from django.contrib.auth.views import LogoutView
# from . import views
#
# urlpatterns = [
#     path('', views.free_table_list, name='free_table_list'),
#     path('add/', views.add_free_table, name='add_free_table'),
#     path('edit/<int:pk>/', views.edit_free_table, name='edit_free_table'),
#     path('delete/<int:pk>/', views.delete_free_table, name='delete_free_table'),
# ]


from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.free_table_list, name='free_table_list'),
    path('add/', views.add_free_table, name='add_free_table'),
    path('edit/<int:pk>/', views.edit_free_table, name='edit_free_table'),
    path('delete/<int:pk>/', views.delete_free_table, name='delete_free_table'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
