from django.contrib import admin
from app.models import Especialistas,paciente,profesional,turnos

# REGISTRAR MODELOS.

admin.site.register(Especialistas)
admin.site.register(paciente)
admin.site.register(profesional)
admin.site.register(turnos)
