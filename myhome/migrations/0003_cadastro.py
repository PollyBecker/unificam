# Generated by Django 3.2.15 on 2022-09-19 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0002_auto_20220918_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('nome_completo', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('meu_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meu_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
