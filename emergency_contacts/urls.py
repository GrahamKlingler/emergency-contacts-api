from django.urls import path
from .views import create_contact, delete_contact

urlpatterns = [
    path('contacts/', create_contact, name='create_contact'),
    path('contacts/<int:id>', delete_contact, name='delete_contact')
]
