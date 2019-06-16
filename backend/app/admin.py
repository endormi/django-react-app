from django.contrib import admin
from .models import Language
from .models import Faangm

"""
Registered models for admin.
Accessable, when logged in.
http://127.0.0.1:8000/admin/
"""
admin.site.register(Language)
admin.site.register(Faangm)
