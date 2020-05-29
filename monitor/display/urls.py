from django.urls import path,include
from . import views
from .views import DataView

#app_name = "api"

urlpatterns = [
    path('', views.index,name='displayy'),
    path('table/', views.index2,name="table-dev"),
    path('api/', DataView.as_view())
]