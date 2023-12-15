from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView, home, dashboard, create_html_file

app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('form/',create_html_file, name='create_html_file')
    # Add more URL patterns as needed
]






