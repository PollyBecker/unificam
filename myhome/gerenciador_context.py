
from .models import Blog, OficinaVideo

def lista_videos_recentes(request):
    lista_videos =OficinaVideo.objects.all().order_by('-lancamento')[0:8]
    print(lista_videos,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    if lista_videos:
        video_destaque = lista_videos[0]
    else:
        video_destaque=None
    print(video_destaque,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return {'lista_videos_recentes':lista_videos, 'video_destaque': video_destaque}


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