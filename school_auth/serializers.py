from rest_framework import serializers
from .models import SchoolAdmin, ExternalAccess
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password

class SchoolAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolAdmin
        fields = ['platformDeveloper', 'groupCategory', 'fullName', 'schoolName', 'schoolAddress', 'contactNumber', 'emailAddress']

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id' ,'name', 'permissions']

class ExternalAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalAccess
        fields = ['admin_name', 'admin_email', 'admin_password']
        extra_kwargs = {
            "admin_password": {"write_only": True}
        }

    def create(self, validate_data):
        validate_data["admin_password"] = make_password(validate_data["admin_password"])
        return super().create(validate_data)
        
