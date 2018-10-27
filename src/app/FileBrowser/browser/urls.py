from django.urls import path
from . import views

app_name = 'browser'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('help/', views.help, name = 'help'),
]
