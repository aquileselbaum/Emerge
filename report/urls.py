from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.report_list, name='report_list'),
    path('', views.report_create, name='report_form'),
    path('chat/', views.chat_view, name='chat'),
]
