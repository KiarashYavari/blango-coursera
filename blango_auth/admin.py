from django.contrib import admin
from blango_auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(User, UserAdmin)
