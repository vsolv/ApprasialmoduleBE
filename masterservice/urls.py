from django.conf import settings
from django.urls import path

from django.conf.urls.static import static
from masterservice.controller import mastercontroller

urlpatterns = [
    path('department', mastercontroller.create_department, name='department'),
    path('department/<id>', mastercontroller.get_department, name='department')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)