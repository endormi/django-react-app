from rest_framework import serializers
from .models import Language
from .models import Faangm


class langSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'paradigm', 'created_by')


class faangmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faangm
        fields = ('id', 'name', 'created', 'location')
