from django.contrib import admin

from imovel.models import Cadastro_Imovel, Cadastro_Cliente, Cadastro_Locacao

# Register your models here.
class Cadastro_ImovelAdmin(admin.ModelAdmin):
    model = Cadastro_Imovel
    list_display = ['tipo_imovel', 'endereco_imovel', 'valor_imovel']
    list_filter = ['tipo_imovel']
admin.site.register(Cadastro_Imovel, Cadastro_ImovelAdmin)


class Cadastro_ClienteAdmin(admin.ModelAdmin):
    model = Cadastro_Cliente
    list_display = ['nome_cliente', 'email_cliente', 'celular_cliente']
    list_filter = ['nome_cliente']
admin.site.register(Cadastro_Cliente, Cadastro_ClienteAdmin)


class Cadastro_LocacaoAdmin(admin.ModelAdmin):
    model = Cadastro_Locacao
    list_display = ['codigo_imovel', 'codigo_cliente', 'inicio_locacao', 'termino_locacao']
admin.site.register(Cadastro_Locacao, Cadastro_LocacaoAdmin)




