from django.db import models

# Create your models here.


class Cliente(models.Model):
    codigo_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=60, verbose_name='Nome')
    email_cliente = models.CharField(max_length=50, verbose_name='Email')
    celular_cliente = models.CharField(max_length=11, verbose_name='Celular')

    def __str__(self):
        return self.nome_cliente

class Imovel(models.Model):

    IMOVEL_CHOICES = (
        (u'casa', u'Casa'),
        (u'apartamento', u'Apartamento'),
        (u'kitnet', u'Kitnet'),
        (u'flat', u'Flat'),
        (u'duplex', u'Duplex'),
        (u'salas', u'Salas'),
        (u'lojas', u'Lojas'),
        (u'galpão', u'Galpão'),
    )

    codigo_imovel = models.AutoField(primary_key=True)
    tipo_imovel = models.CharField(max_length=50, choices=IMOVEL_CHOICES, verbose_name='Tipo')
    endereco_imovel = models.CharField(max_length=100, verbose_name='Endereço')
    valor_imovel = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor')

    def __str__(self):
        return self.tipo_imovel


class Locacao(models.Model):
    codigo_locacao = models.AutoField(primary_key=True)
    codigo_imovel = models.ForeignKey(Imovel, verbose_name='Imóvel', on_delete=models.CASCADE)
    codigo_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    inicio_locacao = models.DateField(verbose_name='Início Locação')
    termino_locacao = models.DateField(verbose_name='Término Locação')

    def __str__(self):
        return self.codigo_locacao


