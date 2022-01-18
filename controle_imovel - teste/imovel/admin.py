from django.contrib import admin
from .models import Imovel, Cliente, Locacao

# Register your models here.

class ImovelAdmin(admin.ModelAdmin):
    model = Imovel
    list_display = ['tipo_imovel', 'endereco_imovel', 'valor_imovel']
    list_filter = ['tipo_imovel']
admin.site.register(Imovel)


class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ['nome_cliente', 'email_cliente', 'celular_cliente']
    list_filter = ['nome_cliente']
admin.site.register(Cliente)


class LocacaoAdmin(admin.ModelAdmin):
    model = Locacao
    list_display = ['codigo_imovel', 'codigo_cliente', 'inicio_locacao', 'termino_locacao']
admin.site.register(Locacao)




