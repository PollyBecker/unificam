from django.contrib import admin
from .models import Homepage, Blog, Usuario, Mensagem, Cadastro, OficinaVideo
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Homepage)
admin.site.register(Blog)
admin.site.register(Mensagem)
admin.site.register(Cadastro)
admin.site.register(OficinaVideo)
admin.site.register(Usuario, UserAdmin)
