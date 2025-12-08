from django.contrib import admin
#
from .models import Medico, Especialidad
# Register your models here.


class MedicoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'especialidad',
        'registro_profesional',
    )


admin.site.register(Medico, MedicoAdmin)



class EspecialidadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
    )


admin.site.register(Especialidad, EspecialidadAdmin)