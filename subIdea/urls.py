from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostCreateView

urlpatterns = [
    path('home/', views.home, name='submissionhome'),
    path('tasks/', views.tasks, name='tasks'),
    path('ideas/', views.ideas, name='ideas'),     
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('poc/new_csv/',views.poccsv, name='poc-csv-create'),
]
