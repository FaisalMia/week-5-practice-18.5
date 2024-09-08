from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('profile/',views.profile,name='profile'),
    path('pass_change/',views.passchange,name='pass_change'),
    path('change_pass/',views.change_pass,name='change_pass'),
]