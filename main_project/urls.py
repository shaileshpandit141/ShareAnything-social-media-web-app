
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authentication import urls as auth_urls
from share_anything import urls as share_anything_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(auth_urls)),
    path('', include(share_anything_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root =  settings.MEDIA_ROOT)