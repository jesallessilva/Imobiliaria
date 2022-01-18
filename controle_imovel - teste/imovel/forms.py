from django import forms
from .models import Cliente, Imovel, Locacao


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'


class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = '__all__'

