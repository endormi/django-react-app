from django.contrib import admin
from django.urls import path
from app.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", test, name="test"),
]
