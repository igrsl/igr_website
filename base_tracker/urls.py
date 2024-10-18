from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('central-government-reform/', include('central_gov.urls')),
    path('local-government-reform/', include('local_gov.urls')),
    path('cso-and-media/', include('cso_media.urls')),
    path('eu-education/', include('eu_education.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
