from django.contrib import admin
#
from .models import User, VerificationCode
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'nombre',
        'apellido',
        'role',
        'is_superuser',
        'is_active',
        'is_staff',
    )    



admin.site.register(User, UserAdmin)



class CodeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'code',
        'created',
        'modified',
    )


admin.site.register(VerificationCode, CodeAdmin)