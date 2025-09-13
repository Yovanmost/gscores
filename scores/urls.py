from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("check-score/", views.check_score, name="check_score"),
    path("report/", views.report, name="report"),
    path("top-group-a/", views.top_group_a, name="top_group_a"),
]
