from django.urls import path,include
from .import views
app_name='app1'

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login', views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('afterl',views.afterl,name='afterl'),
    path('npage',views.npage,name='npage'),
    path('success_page/', views.success_page, name='success_page'),
    #path('base/', views.base, name='base'),
    path('test1/', views.test1, name='test1'),
    path('base/', views.dtest1, name='dtest1'),
    path('t10/', views.t10, name='t10'),
       
    
     
   
  
]
