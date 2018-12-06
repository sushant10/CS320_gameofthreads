from django.urls import path
from . import views

app_name = 'browser'
urlpatterns = [
    path('', views.default, name = 'default' ),
    path('help/', views.help, name = 'help'),
    path('systems/dt/', views.dtSystems.as_view(), name = 'dt'),
    path('systems/<int:serialNumberInserv>', views.files, name = 'files'),
    path('systems/', views.systems, name = 'systems' ),
    path('download/<slug:fileID>', views.download, name = 'download'),
    path('login/', views.loginView, name = 'login' ),
	path('logout/', views.logoutView, name = 'logout' )
]
