from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('index/', views.index,name='index'),
    path('logout/', views.logout,name='logout'),
    ##RestAPI URL'S
    path('userinfo/', views.UserProfileList.as_view()),
    path('profile/<str:id>',views.api_profile_view,name='profile'),
    path('profile_update/<str:id>',views.api_profile_update,name='update'),
    path('profile_delete/<str:id>',views.api_profile_delete,name='delete'),
    path('profile_add/<str:id>',views.api_profile_add,name='add'),
]