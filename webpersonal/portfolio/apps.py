from django.apps import AppConfig

# CREAMOS LA CLASE PARA EL CAMBIO DE NOMBRE A ESPAÑOLS
class PortfolioConfig(AppConfig):
    name = 'portfolio'
    verbose_name = 'portafolio'