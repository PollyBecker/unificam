# Generated by Django 3.2.15 on 2022-09-19 03:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('visualizado', models.BooleanField(default=False)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('mensagem', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='OficinaVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tilulo', models.CharField(max_length=100)),
                ('visualizados', models.IntegerField(default=0)),
                ('lancamento', models.DateTimeField(default=django.utils.timezone.now)),
                ('thumb', models.ImageField(upload_to='thumb')),
                ('descricao', models.TextField(max_length=1000)),
                ('categoria', models.CharField(choices=[('OFICINA', 'Oficina'), ('FAMILIA', 'Família'), ('LIVE', 'Live')], max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='videos_vistos',
            field=models.ManyToManyField(to='myhome.OficinaVideo'),
        ),
    ]