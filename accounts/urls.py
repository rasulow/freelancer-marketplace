from django.urls import path
from . import views


urlpatterns = [
    path('sign-in/', views.SignIn.as_view(), name='sign-in'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('navigator/', views.Navigator.as_view(), name='navigator'),
    path('company-signup/', views.CompanySignUp.as_view(), name='company-signup'),
    path('freelancer-signup/', views.FreelancerSignUp.as_view(), name='freelancer-signup'),
    path('verification/', views.Verification.as_view(), name='verification'),
    path('profile/', views.Profile.as_view(), name='profile'),
]