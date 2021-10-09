from django.urls import path
from ProyectoWeb import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name="Home"),
    path('tienda',views.tienda, name="Tienda"),
    #path('admin',views.registro, name="admin"),
    
    path('registrar',views.registro, name="registrar"),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)