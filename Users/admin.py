from django.contrib import admin
from Users.models import Users
# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    pass

admin.register(Users,UsersAdmin)