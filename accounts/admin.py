from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ("email", "first_name", "last_name", "is_active")
    ordering = ("-date_joined",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(Company_info)
admin.site.register(Designation)
admin.site.register(Shift)
admin.site.register(User_details)
admin.site.register(Pi_attendance)
admin.site.register(Pi_users)
