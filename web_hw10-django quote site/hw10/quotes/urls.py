from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('author/<str:fullname>',views.author_about,name='author_about'),
    path('new_author/', views.new_author, name='new_author'),
    path('new_quote/', views.new_quote, name='new_quote'),
    path('tag/<str:name>/', views.tag_info, name='tag_info'),
    path('tag/<str:name>/<int:page>/', views.tag_info, name='tag_paginate'),
    path('get_data/', views.get_data, name='get_data'),
]