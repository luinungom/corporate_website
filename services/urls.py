from django.urls import path

from . import views as service_views

from django.conf import settings

urlpatterns = [

    path('', service_views.services, name='services'),

]

# For media
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
