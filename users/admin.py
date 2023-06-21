from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from users.models import User
# Register your models here.

class UserAdmin(DjangoUserAdmin):
    model=User
    list_display=(
        'email','username','is_staff','is_superuser','is_active',
    )

    list_editable=(
        'is_active','is_staff','is_superuser'
    )

    fieldsets=(
        (
            None,{
                "fields":("email","username","password")
            }
        ),
        (
            "Permissions",{
                "fields":("is_staff","is_active","is_superuser",)
            }
        ),
    )

    add_fieldsets=(
        (None,{
            "fields":("email","username","password1","password2","is_staff","is_active","groups","user_permissions")
        }),
    )

    search_fields=('email','username')
    ordering=('email',)

admin.site.register(User,UserAdmin)