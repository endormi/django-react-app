from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('languages', views.langView)
router.register('faangm', views.faangmView)


urlpatterns = [
    path('', include(router.urls)),
]
