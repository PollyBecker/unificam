from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
# criar filmes

class Homepage(models.Model):
    tilulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    endereco_rua=models.CharField(max_length=100)
    endereco_bairro=models.CharField(max_length=100)
    encereco_cep=models.CharField(max_length=100)
    endereco_cidade=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    insta_link=models.CharField(max_length=100,default='#')
    face_link=models.CharField(max_length=100,default='#')

    def __str__(self):
        return self.tilulo

LISTA_CATEGORIAS=(
    ('EVENTO', 'Eventos'),
    ('FAMILIA', 'Família'),
    ('NOVIDADE', 'Novidades'),
    ('INFORMATIVO', 'Informativos'),
    ('SAUDE', 'Saúde'),
    ('OUTROS', 'Outros')
)


class Blog(models.Model):
    tilulo = models.CharField(max_length=100)
    visualizados = models.IntegerField(default=0)
    data = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(upload_to='media')
    texto = models.TextField(max_length=1000)
    categoria =models.CharField(max_length=20,choices=LISTA_CATEGORIAS)

    def __str__(self):
        return self.tilulo


class Usuario(AbstractUser):

    blog_vistos = models.ManyToManyField('Blog')
    videos_vistos = models.ManyToManyField('OficinaVideo')

    def __str__(self):
        return self.email


LISTA_CATEGORIAS=(
    ('OFICINA', 'Oficina'),
    ('FAMILIA', 'Família'),
    ('LIVE', 'Live'),
)


class OficinaVideo(models.Model):
    tilulo=models.CharField(max_length=100)
    visualizados =models.IntegerField(default=0)
    lancamento=models.DateTimeField(default=timezone.now)
    thumb=models.ImageField(upload_to='thumb')
    video = models.URLField(default='')
    descricao=models.TextField(max_length=1000)
    categoria=models.CharField(max_length=20,choices=LISTA_CATEGORIAS)

    def __str__(self):
        return self.tilulo

class Mensagem(models.Model):
    email=models.CharField(max_length=100)
    visualizado =models.BooleanField(default=False)
    data=models.DateTimeField(default=timezone.now)
    nome=models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    mensagem = models.TextField(max_length=1000)

    def __str__(self):
        return self.nome
class Cadastro(models.Model):
    meu_usuario=models.ForeignKey("Usuario", related_name="meu_usuario", on_delete=models.CASCADE)
    data=models.DateTimeField(default=timezone.now)
    nome_completo=models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)


    def __str__(self):
        return self.nome_completo
