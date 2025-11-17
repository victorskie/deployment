from django.urls import path
from . import views


urlpatterns = [
    path('Signup', views.Sigup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('course_list', views.course_list, name='course_list'),
    path('course_description/<int:course_id>/', views.course_description, name='course_description'),
]