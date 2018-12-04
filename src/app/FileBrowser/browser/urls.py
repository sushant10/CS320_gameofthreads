from django.urls import path
from . import views

app_name = 'browser'
urlpatterns = [
    path('', views.systems, name = 'systems' ),
    path('help/', views.help, name = 'help'),
    path('systems/<int:serialNumberInserv>', views.files, name = 'files'),
    path('systems/', views.systems, name = 'systems' ),
    path('login/', views.loginView, name = 'login' ),
    path('logout/', views.logoutView, name = 'logout' ),
    path('dt/', views.dtSystems.as_view(), name = 'dt' )
]
