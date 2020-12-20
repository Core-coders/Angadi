from django.contrib import admin
from .models import User
# Register your models here.
class UserImp(admin.ModelAdmin):
    list_display = ('username','user_type' )

admin.site.register(User, UserImp)