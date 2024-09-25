from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=17)

    def __str__(self):
        return self.last_name + ", " + self.first_name
