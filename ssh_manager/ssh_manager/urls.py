from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('blog.urls')),
    path('ssh_manager/', include('ssh_connections_app.urls')),
    path('admin/', admin.site.urls),
]


