from django.urls import path
from features import views

urlpatterns = [
    path('', views.home, name='index'),
    path('job/', views.job, name='job'),
    path('apply/', views.apply, name='apply'),
    path('apply/applying/', views.applying, name='applying'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('resume/resume2/', views.resume, name='resume'),
    path('resume1/', views.resume1, name='resume1'),
    path('resume2/', views.resume2, name='resume2'),
    path('blog/', views.blog, name='blog'),
    path('view_blog/', views.view_blog, name='view_blog'),
    path('blog/view_blog/', views.blog, name='view_blog'),
    path('updateprofile/', views.update_profile, name='updateprofile'),
    path('updateprofile/profile/', views.update_profile, name='updateprofile'),
    path('job/contact/', views.contact, name='contact'),
    path('contact/', views.contact, name='contact'),
]
