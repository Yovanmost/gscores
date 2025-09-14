from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("check-score/", views.check_score, name="check_score"),
    path("report/", views.report, name="report"),
    path("top-group-a/", views.top_group_a, name="top_group_a"),

    path('api/top-group-a/', views.top_group_a_api, name='top_group_a_api'),
    path('api/check-score/', views.check_score_api, name='check_score_api'),
    path('api/report/', views.report_api, name='report_api'),
    path('api/', views.home_api, name='home_api'),
]
