# jobs/urls.py
from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/', views.post_job, name='post_job'),
    path('list/', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('applications/<int:job_id>/', views.job_applications, name='job_applications'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
    path('my-applications/', views.user_job_applications, name='user_job_applications'),
    path('profile/', views.profile, name='profile'),


]
