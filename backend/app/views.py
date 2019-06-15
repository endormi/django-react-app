from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import langSerializer
from .models import Faangm
from .serializers import faangmSerializer


class langView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = langSerializer


class faangmView(viewsets.ModelViewSet):
    queryset = Faangm.objects.all()
    serializer_class = faangmSerializer
