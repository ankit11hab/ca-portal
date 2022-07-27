
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# making admin non accessible my non staff users
from .admin import admin_view
admin.site.admin_view = admin_view
#login, go to left navbar to access admin
urlpatterns = [
    path('admin65G9fKjL/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('dashboard.urls')),
    path('submissions/', include('submissions.urls')),
    

   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

handler404 = 'ca_portal.views.error_404'
handler500 = 'ca_portal.views.error_500'