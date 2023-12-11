
from django.contrib import admin
from django.urls import path, include
from Appcoder.views import  show_html,  crear_persona

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('Appcoder.urls')),
    path('accounts/', include('accounts.urls'))
]
