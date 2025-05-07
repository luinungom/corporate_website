from django.urls import path
from . import views as pages_views


from django.conf import settings

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', pages_views.pages, name='page'),

]

# For media
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)