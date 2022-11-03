from django.shortcuts import render, redirect, reverse
from .models import Blog, OficinaVideo,Usuario
from django.views.generic import ListView, DetailView, FormView,CreateView
from .forms import CriarContaForm, FormHome, ContatoForm, CadastroForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# fbv function based views
# def homepage(request):
#     return render(request, 'homepage.html')
#cbv class based views

class Homepage( ListView):
    template_name = 'homepage.html'
    model = Blog

class ListaBlog( ListView):
    template_name = 'listablog.html'
    model = Blog

class DetalhesBlog( DetailView ):
    template_name = 'blog.html'
    model = Blog
    #list_view me retorna uma lista com nome object_list
from django.shortcuts import render

# Create your views here.
class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('myhome:login')

class Contato(CreateView):
    template_name = 'contato.html'
    form_class = ContatoForm

    def form_valid(self, form):
        print(form)
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('myhome:homepage')
class Cadastro(CreateView):
    template_name = 'cadastro.html'
    form_class = CadastroForm

    def form_valid(self, form):
        formulario = form.save(commit=False)
        formulario.meu_usuario = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('myhome:login')


class HomeOficina(ListView):
    template_name = 'oficinas.html'
    model = OficinaVideo

    def get(self, request, *args, **kwargs):
        # contabilizando as views

        return super().get(request, *args, **kwargs)

    #list_view me retorna uma lista com nome object_list


class DetalhesOficina(LoginRequiredMixin, DetailView):
    template_name = 'detalhesoficinas.html'
    model = OficinaVideo

    # detailview me retorna a variavel object

    def get(self, request, *args, **kwargs):
        # contabilizando as views
        video = self.get_object()
        video.visualizados += 1
        video.save()
        usuario = request.user
        usuario.videos_vistos.add(video)
        return super().get(request, *args, **kwargs)


class HomeOficina( LoginRequiredMixin, ListView):
    template_name = 'oficinas.html'
    model = OficinaVideo
    #list_view me retorna uma lista com nome object_list

class Sobre(ListView):
    template_name = 'sobre.html'
    model = Usuario
    #list_view me retorna uma lista com nome object_list


class Doe(ListView):
    template_name = 'doe.html'
    model = Usuario
    #list_view me retorna uma lista com nome object_list