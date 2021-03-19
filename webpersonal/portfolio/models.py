from django.db import models

# Create your models here. OSEA LOS MODELOS DE LOS PROYECTOS O TABLAS DE PROYECTOS
# Y CON EL VERBOSE_NAME CAMBIAMOS AL ESPAÑOL
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Título")
    description = models.TextField(verbose_name = "Descripción")
    # EL UPLOADTOP ES PARA TENER Y ALMACENAR LOS ARCHIVOS JPG EN PROJECTS Y SEPARARLOS X ETIQUETA
    image = models.ImageField(verbose_name = "Imagen", upload_to = "projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Edición")

# PARA Q APAREZCAN EN ESPAÑOL Y CORREGIDOS LOS NOMBRES
    class Meta: 
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created"]
        # PARA Q APAREZCAN LOS NOMBRES DE LOS PROYECTOS EN VES DELO INGKES Q APARECE
    def __str__(self):
        return self.title