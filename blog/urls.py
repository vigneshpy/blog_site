from django.urls import path
from blog import views 

urlpatterns=[
path('',views.index,name='index'),
 path('create',views.create,name='create'),
path('logout',views.logout_,name='logout_'),
path('login',views.login,name='login'),
path('signup',views.signup,name='signup'),
]