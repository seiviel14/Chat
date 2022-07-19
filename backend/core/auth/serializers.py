from typing_extensions import Required
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist

from core.user.serializers import UserSerializer
from core.user.models import User

class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, Required=True)
    email = serializers.EmailField(max_length=128, write_only=True, Required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_active', 'created', 'updated']

    def create(self, data_validated):
        try:
            user = User.objects.get(email=data_validated['email'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**data_validated)
        
        return user