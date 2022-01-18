from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'imovel'

urlpatterns = [
   path('', TemplateView.as_view, name='index'),
   path('cliente/', views.ClienteCreate.as_view(), name='cliente_create'),
   path('listacliente/', views.ClienteList.as_view(), name='cliente_list'),
   path('listaimovel/', views.ImovelList.as_view(), name='imovel_list'),
   path('imovel/', views.ImovelCreate.as_view(), name='imovel_create'),
   path('listalocacao/', views.LocacaoList.as_view(), name='locacao_list'),
   path('locacao/', views. LocacaoCreate.as_view(), name='locacao_create'),
]
