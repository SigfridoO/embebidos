from django.contrib import admin

from .models import Memoria

class MemoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')

admin.site.register(Memoria, MemoriaAdmin)
