from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Cliente, Imovel, Locacao
from django.urls import reverse_lazy
# Create your views here.


class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()


class ImovelList(ListView):
    model = Imovel
    queryset = Imovel.objects.all()


class LocacaoList(ListView):
    model = Locacao
    queryset = Locacao.objects.all()


class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('index')


class ImovelCreate(CreateView):
    model = Imovel
    fields = '__all__'
    success_url = reverse_lazy('index')


class LocacaoCreate(CreateView):
    model = Locacao
    fields = '__all__'
    success_url = reverse_lazy('index')


