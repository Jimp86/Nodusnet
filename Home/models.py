from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.

class Principal(models.Model):
    logo = models.ImageField(upload_to="logos")
    color_interfaz = models.CharField(default="Verde",
                                    max_length=100,
                                    choices=(
                                        ("/static/css/colors/green.css","Verde"),
                                        ("/static/css/colors/mossgreen.css", "Verde Mostaza"),
                                        ("/static/css/colors/bridge.css", "Verde Claro"),
                                        ("/static/css/colors/orange.css","Naranja"),
                                        ("/static/css/colors/pink.css","Rosado"),
                                        ("/static/css/colors/red.css","Rojo"),
                                        ("/static/css/colors/purple.css","Morado"),
                                        ("/static/css/colors/yellow.css", "Amarillo"),
                                        ("/static/css/colors/violet.css", "Violeta"),
                                        ("/static/css/colors/cyan.css", "Cyan"),
                                        ("/static/css/colors/azul.css", "Azul"),
                                            )
                                    )
    video_fondo = models.CharField(max_length=120, default="J2qDRJdTGow")

    class Meta:
        verbose_name_plural = "1. Página Principal"

class DatosPrincipales(models.Model):
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=60)
    email = models.EmailField(max_length=120)
    whatsapp = models.URLField(max_length=500, null=True, blank=True)
    facebook = models.URLField(max_length=500,null=True,blank=True)
    instagram = models.URLField(max_length=500,null=True,blank=True)
    youtube = models.URLField(max_length=500,null=True,blank=True)

    class Meta:
        verbose_name_plural = "1.1 Datos de la Aplicación"


class Slider(models.Model):
    imagen = models.ImageField(upload_to="Slider")
    frase1 = models.CharField(max_length=100)
    posicion_frase1 = models.IntegerField(default=50)
    frase2 = models.CharField(max_length=100)
    posicion_frase2 = models.IntegerField(default=50)
    texto_decorativo = models.CharField(max_length=100)
    posicion_texto_decorativo = models.IntegerField(default=50)
    izquierda = models.BooleanField(default=True)
    derecha = models.BooleanField(default=False)
    centro = models.BooleanField(default=False)
    duracion = models.IntegerField(default=9)
    text_size = models.IntegerField(default=100)

    class Meta:
        verbose_name_plural = "1.2 Sliders"


class Servicio(models.Model):
    titulo = models.CharField(max_length=60)
    titulo2 = models.CharField(max_length=30, null=True, blank=True)
    titulo3 = models.CharField(max_length=30, null=True, blank=True)
    concepto = models.TextField(max_length=200)
    nota = models.TextField(max_length=60)
    imagen = models.ImageField(upload_to="Servicio")

    class Meta:
        verbose_name_plural="2. Servicio"


class Caracteristicas(models.Model):
    icono = models.CharField(max_length=40)
    nombre = models.CharField(max_length=60)
    detalle = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural="2.1 Características"


class Cobertura(models.Model):
    titulo = models.CharField(max_length=60)
    titulo2 = models.CharField(max_length=30, null=True, blank=True)
    titulo3 = models.CharField(max_length=30, null=True, blank=True)
    concepto = models.TextField(max_length=200)
    nota = models.TextField(max_length=60)
    imagen = models.ImageField(upload_to="Datos")

    class Meta:
        verbose_name_plural="2.2 Cobertura"


class Metricas(models.Model):
    icono = models.CharField(max_length=40)
    nombre = models.CharField(max_length=60)
    detalle = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural="2.3 Métricas"


class Sitios(models.Model):
    icono = models.CharField(max_length=40)
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural="2.4 Sitios"


class Planes(models.Model):
    titulo = models.CharField(max_length=60, null=True, blank=True)
    titulo2 = models.CharField(max_length=30, null=True, blank=True)
    titulo3 = models.CharField(max_length=30, null=True, blank=True)
    concepto = models.TextField(max_length=200, null=True, blank=True)
    nota = models.TextField(max_length=60, null=True, blank=True)
    imagen = models.ImageField(upload_to="Planes", null=True, blank=True)

    class Meta:
        verbose_name_plural="3. Planes"


class Aplicaciones(models.Model):
    nombre = models.CharField(max_length=60)
    detalle = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to="Aplicaciones")

    class Meta:
        verbose_name_plural="3.2 Aplicaciones Planes"


class ListaPlanes(models.Model):
    #categoria = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    icono = models.CharField(max_length=20, choices=(("fa fa-home", "fa fa-home"), ("fa fa-archive", "fa fa-archive"), ("fa fa-gamepad", "fa fa-gamepad"), ("fa fa-camera", "fa fa-camera")))
    nombre = models.CharField(max_length=20, choices=(("Básico", "Básico"), ("Standard", "Standard"), ("Premiun", "Premium"), ("Experto", "Experto")))
    megas = models.CharField(max_length=20, choices=(("20 Mbps", "20 Mbps"), ("30 Mbps", "30 Mbps"), ("60 Mbps", "60 Mbps"), ("100 Mbps", "100 Mbps")))
    precio = models.CharField(max_length=10, choices=(("20.00", "20.00"), ("25.00", "25.00"), ("35.00", "35.00"), ("60.00", "60.00")))
    conexion = models.CharField(default="Simétrica", max_length=20)
    comparticion = models.CharField(default="1:1", max_length=10)
    dispositivos = models.CharField(max_length=20, choices=(("4", "4"), ("8", "8"), ("15", "15"), ("25", "25")))
    info = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "3.1 Lista Planes"


class Promociones(models.Model):
    imagen = models.ImageField(upload_to="Promociones", null=True, blank=True)
    titulo=models.CharField(max_length=100, null=True, blank=True)
    contenido=models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural="4. Promociones"


class Nodusnet(models.Model):
    titulo = models.CharField(max_length=60)
    titulo2 = models.CharField(max_length=30, null=True, blank=True)
    titulo3 = models.CharField(max_length=30, null=True, blank=True)
    concepto = models.TextField(max_length=400)
    nota = models.TextField(max_length=100)
    imagen = models.ImageField(upload_to="Nodusnet")

    class Meta:
        verbose_name_plural="5. Nodusnet"


class Nosotros(models.Model):
    icono=models.CharField(max_length=30)
    titulo=models.CharField(max_length=100, null=True, blank=True)
    contenido=models.TextField(max_length=400, null=True, blank=True)

    class Meta:
        verbose_name_plural="5.1 Nosotros"







