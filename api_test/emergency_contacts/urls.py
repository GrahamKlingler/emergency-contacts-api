from django.urls import path
from .views import get_contacts, create_contact, delete_contact

urlpatterns = [
    path('contacts/', create_contact, name='create_contact'),
    path('contacts/showall', get_contacts, name='get_contacts'),
    path('contacts/<int:id>', delete_contact, name='delete_contact')
]
