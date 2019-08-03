from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name="home"),
path('log/',views.log,name="log"),
path('log/login/',views.login,name="login"),
#path('<list_id>',views.delete,name="delete"),
path('log/signup/',views.signup,name="signup"),
path('logout/',views.logout,name="logout"),
path('delete/<list_id>',views.delete,name="delete"),
path('edit/<list_id>',views.edit,name="edit"),
path('edit_msg/<list_id>/',views.edit_msg,name="edit_msg"),

path('uncross/<list_id>',views.uncross,name="uncross"),

]
