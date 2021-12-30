from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'firstName', 'lastName',
                  'photo', 'is_active', 'is_staff')
