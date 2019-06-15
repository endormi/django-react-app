from rest_framework import serializers
from .models import Language


class langSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'paradigm', 'created_by')
