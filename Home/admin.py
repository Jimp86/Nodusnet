from django.contrib import admin

# Register your models here.
from Nodus.snippers import Attr
from Home.models import *

@admin.register(Principal)
class AdminPrincipal(admin.ModelAdmin):
    list_display_links = Attr(Principal)
    list_display = Attr(Principal)


@admin.register(DatosPrincipales)
class AdminDatosPrincipales(admin.ModelAdmin):
    list_display_links = Attr(DatosPrincipales)
    list_display = Attr(DatosPrincipales)


@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display_links = Attr(Slider)
    list_display = Attr(Slider)


@admin.register(Servicio)
class Admin_Servicio(admin.ModelAdmin):
    list_display_links = Attr(Servicio)
    list_display = Attr(Servicio)


@admin.register(Caracteristicas)
class Admin_Caracteristicas(admin.ModelAdmin):
    list_display_links = Attr(Caracteristicas)
    list_display = Attr(Caracteristicas)


@admin.register(Cobertura)
class Admin_Cobertura(admin.ModelAdmin):
    list_display_links = Attr(Cobertura)
    list_display = Attr(Cobertura)


@admin.register(Metricas)
class Admin_Metricas(admin.ModelAdmin):
    list_display_links = Attr(Metricas)
    list_display = Attr(Metricas)


@admin.register(Sitios)
class Admin_Sitios(admin.ModelAdmin):
    list_display_links = Attr(Sitios)
    list_display = Attr(Sitios)


@admin.register(Planes)
class AdminPlanes(admin.ModelAdmin):
    list_display_links = Attr(Planes)
    list_display = Attr(Planes)


@admin.register(Aplicaciones)
class Admin_Aplicaciones(admin.ModelAdmin):
    list_display_links = Attr(Aplicaciones)
    list_display = Attr(Aplicaciones)


@admin.register(ListaPlanes)
class Admin_ListaPlanes(admin.ModelAdmin):
    list_display_links = Attr(ListaPlanes)
    list_display = Attr(ListaPlanes)


@admin.register(Promociones)
class Admin_Promociones(admin.ModelAdmin):
    list_display_links = Attr(Promociones)
    list_display = Attr(Promociones)


@admin.register(Nodusnet)
class Admin_Nodusnet(admin.ModelAdmin):
    list_display_links = Attr(Nodusnet)
    list_display = Attr(Nodusnet)


@admin.register(Nosotros)
class Admin_Nosotros(admin.ModelAdmin):
    list_display_links = Attr(Nosotros)
    list_display = Attr(Nosotros)
