from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signupuser, name='signup'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>/edit/', views.edit_quote, name='edit_quote'),
    path('profile/<int:pk>/delete/', views.delete_quote, name='delete_quote'),
]