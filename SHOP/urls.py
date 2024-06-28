from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("" , views.INDEX , name="SHOP"),
    path("HOME/" , views.HOME , name="HOME"),
    path("CONTACT" , views.CONTACTS , name="CONTACT US"),
    path("TRACKER" , views.TRACKER, name="TRACKING STATUS"),
    path("SEARCH" , views.SEARCH , name="SEARCH"),
    path("PRODUCT_VIEW/<int:id>" , views.PRODUCT_VIEW , name="PRODUCT_VIEW"),
    path("CHECKOUT" , views.CHECKOUT , name="CHECKOUT"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
