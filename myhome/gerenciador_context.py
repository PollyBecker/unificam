
from .models import Blog, OficinaVideo


def lista_filmes_recentes(request):
    lista_filmes = OficinaVideo.objects.all().order_by('-lancamento')[0:8]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {'lista_filmes_recentes': lista_filmes, 'filme_destaque': filme_destaque}


def lista_filmes_alta(request):
    lista_filmes = OficinaVideo.objects.all().order_by('-visualizados')[0:8]
    return {'lista_filmes_alta': lista_filmes}

def lista_blog_recentes(request):
    lista_blog =Blog.objects.all().order_by('-data')[0:6]
    if lista_blog:
        blog_destaque = lista_blog[0]
    else:
        blog_destaque=None
    return {'lista_blog_recentes':lista_blog, 'blog_destaque': blog_destaque}

def lista_blog_alta(request):
    lista_blog =Blog.objects.all().order_by('-visualizados')[0:3]
    return {'lista_blog_alta': lista_blog }