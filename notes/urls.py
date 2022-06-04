from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.index, name='home-page'),
    path('topics/', views.topics, name='topics'),
    path('entries/<int:topic_id>/', views.entries, name='entries'),
]
