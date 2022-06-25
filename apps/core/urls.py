from django.urls import path
from .views import index, contacts, about

urlpatterns = [
    path('', index, name="index"),
    path('contacts/', contacts, name="contacts"),
    path('about/', about, name="about"),
]
