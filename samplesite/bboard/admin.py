from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Bd, Rubric, CustomUser, comment
from django.utils.translation import gettext_lazy as _



class BdAdmin(admin.ModelAdmin):
    list_display = ['rubric', 'title', 'content', 'price', 'published'] 
    list_display_links = ['title', 'content', 'rubric']
    search_fields = ['title', 'content']     

class RubricAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']    


class commentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'text']
    list_display_links = ['user', 'post']
    search_fields = ['user', 'post']


class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ["username", "email", "first_name", "last_name", "is_staff", 'birth_date', 'phone_number']
    list_display_links = ['username']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", 'phone_number', 'birth_date')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Bd, BdAdmin)
admin.site.register(Rubric, RubricAdmin)
admin.site.register(comment, commentAdmin)




# @admin.register(CustomUser)
# class UserAdmin(BaseUserAdmin):
#     model = CustomUser
#     list_display = ("username", "email", "first_name", "last_name", "is_staff", 'birth_date')
    
    



