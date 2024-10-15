from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomerUserCreationForm,CustomUserChangeForm
from .models import CustomUser, UserProfile


class CustomUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email","username"]


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(UserProfile)