from django.urls import path
from accounts import views
urlpatterns=[

path('signup/',views.signup,name='signup'),
path('login/',views.login,name='login'),
path('logout_/',views.logout_,name='logout_')


]