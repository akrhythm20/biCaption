from django.urls import path
from Hub import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register1', views.register_step1, name='register1'),
    path('register2', views.register_step2, name='register2'),
    path('login', views.loginUser, name='login'),
    path('glogin', views.googleLogin, name='glogin'),
    path('role', views.role, name='role'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logoutUser, name='logout'),
    path('category', views.category, name="category"),
    path('allfromCat/<str:cat>', views.allfromCat, name="allfromCat"),
    path('blog/<int:pid>', views.blog, name="blog"),
    path('appointment/<int:pid>', views.appointment, name="appointment"),
    path('createAppointment', views.createAppointment, name="createAppointment"),
    path('pagination<int:bnum>', views.pagination, name="pagination"),
]