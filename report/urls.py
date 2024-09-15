from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.report_list, name='report_list'),
    path('', views.submit_report, name='submit_report'),
    path('report_summary/<int:report_id>/', views.report_summary, name='report_summary'),
    path('resolve/<int:report_id>/', views.mark_resolved, name='mark_resolved'),
]

