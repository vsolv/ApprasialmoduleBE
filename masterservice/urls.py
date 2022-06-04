from django.conf import settings
from django.urls import path

from django.conf.urls.static import static
from masterservice.controller import mastercontroller

urlpatterns = [
    path('department', mastercontroller.create_department, name='department'),
    path('department/<id>', mastercontroller.get_department, name='department'),
    path('country', mastercontroller.country, name='country'),
    path('country/<id>', mastercontroller.get_country, name='country'),
    path('state', mastercontroller.state, name='state'),
    path('state/<id>', mastercontroller.get_state, name='state'),
    path('district', mastercontroller.district, name='district'),
    path('district/<id>', mastercontroller.get_district, name='district'),
    path('city', mastercontroller.city, name='city'),
    path('city/<id>', mastercontroller.get_city, name='city'),
    path('pincode', mastercontroller.pincode, name='pincode'),
    path('pincode/<id>', mastercontroller.get_pincode, name='pincode'),
    path('goal', mastercontroller.goal, name='goal'),
    path('goal/<id>', mastercontroller.get_goal, name='goal')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)