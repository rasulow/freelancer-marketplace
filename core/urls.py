from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('sign-in/', views.SignIn.as_view(), name='sign-in'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('navigator/', views.Navigator.as_view(), name='navigator'),
]