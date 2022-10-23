from django.urls import path
from . import views

urlpatterns = [
    path('referal_id/', views.points_referal_id,name='points-referal'), # api takes alcherid and points in data
]