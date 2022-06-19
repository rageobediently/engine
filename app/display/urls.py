from django.urls import path,include
from . import views

app_name = "display"

urlpatterns = [
    path('', views.index, name='display'),
    path('table/', views.index2, name="table-dev"),
    path('api/metrics/', views.MetricListAPI.as_view()),
    path('api/metrics/add', views.MetricCreateAPI.as_view()),
]