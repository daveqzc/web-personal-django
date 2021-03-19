from django.contrib import admin

# IMPORTAMOS LA CLASE CREADA EN EL MODELS.PY
from .models import Project
# Register your models here.
# CREAMOS UNA CLASE INDICAANDO LOS ATRIBUTOS DE SOLO LECTURA
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# HICIMOS EL REGSTRO DEL PROYECTO ENICANDOLE LOS 2 ATRIBUTOS ESPECIALES
admin.site.register(Project, ProjectAdmin)

