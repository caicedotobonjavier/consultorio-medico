from django.contrib import admin
#
from .models import Cita
# Register your models here.


class CitaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'medico',
        'paciente',
        'fecha_cita',
        'hora_cita',
        'duracion_minutos',
        'motivo_cita',
        'estado',
    )


admin.site.register(Cita, CitaAdmin)