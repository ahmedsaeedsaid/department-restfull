from rest_framework import serializers
from .models import Department
from django.contrib.auth.models import User


class DepartmentSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Department
        fields = ('id', 'name', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    departments = serializers.PrimaryKeyRelatedField(many=True, queryset=Department.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'departments')
