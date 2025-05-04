from django.urls import path
from . import views as blog_views

from django.conf import settings

urlpatterns = [
    path('', blog_views.blog, name='blog'),

]

# For media
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)