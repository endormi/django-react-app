from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import langSerializer


class langView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = langSerializer
