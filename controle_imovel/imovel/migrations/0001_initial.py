# Generated by Django 2.1.4 on 2022-01-16 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro_Cliente',
            fields=[
                ('codigo_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome_cliente', models.CharField(max_length=60, verbose_name='Nome')),
                ('email_cliente', models.CharField(max_length=50, verbose_name='Email')),
                ('celular_cliente', models.CharField(blank=True, max_length=11, null=True, verbose_name='Celular')),
            ],
        ),
        migrations.CreateModel(
            name='Cadastro_Imovel',
            fields=[
                ('codigo_imovel', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_imovel', models.CharField(choices=[('casa', 'Casa'), ('apartamento', 'Apartamento'), ('kitnet', 'Kitnet'), ('flat', 'Flat'), ('duplex', 'Duplex'), ('salas', 'Salas'), ('lojas', 'Lojas'), ('galpão', 'Galpão')], max_length=50, verbose_name='Tipo')),
                ('endereco_imovel', models.CharField(max_length=100, verbose_name='Endereço')),
                ('valor_imovel', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Cadastro_Locacao',
            fields=[
                ('codigo_locacao', models.AutoField(primary_key=True, serialize=False)),
                ('inicio_locacao', models.DateField(verbose_name='Início Locação')),
                ('termino_locacao', models.DateField(verbose_name='Término Locação')),
                ('codigo_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imovel.Cadastro_Cliente')),
                ('codigo_imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imovel.Cadastro_Imovel', verbose_name='Imóvel')),
            ],
        ),
    ]
