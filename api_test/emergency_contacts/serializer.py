from rest_framework import serializers
from .models import Contact
import re

class ContactSerializer(serializers.ModelSerializer):
    # validate phone number
    def phone_valid(self, phone_number):
        regex = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
        return re.search(regex, phone_number)

    # validate all fields
    def validate(self, data):
        name_match = re.compile(r"^[a-zA-Z-]*$")
        phone = data['phone_number']
        if len(data['first_name']) == 0:
            raise serializers.ValidationError("first_name is empty")
        elif len(data['last_name']) == 0:
            raise serializers.ValidationError("last_name is empty")
        elif not re.match(name_match, data['first_name']) or not re.match(name_match, data['last_name']):
            raise serializers.ValidationError("names can only include letters and dashes")
        elif len(data['phone_number']) < 10:
            raise serializers.ValidationError("phone_number must be at least 10 characters")
        elif not self.phone_valid(data['phone_number']):
            raise serializers.ValidationError("phone_number must be valid form. ex. (888) 888-8888, 888-888-8888, 8888888888")
        
        return data

    # transform Contact to json MetaData
    class Meta:
        model = Contact
        fields = '__all__'
