from django.urls import path, include, reverse_lazy
from .views import Homepage, DetalhesBlog, CriarConta, HomeOficina, DetalhesOficina, Contato, Cadastro,Sobre,ListaBlog
from django.contrib.auth import views as auth_views

app_name= 'myhome'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path("blog/<int:pk>", DetalhesBlog.as_view(),name='detalhesblog'),
    path("blog/", ListaBlog.as_view(), name='listablog'),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path("criarconta/", CriarConta.as_view(), name='criarconta'),
    path("contato/", Contato.as_view(), name='contato'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path("cadastro/", Cadastro.as_view(), name='cadastro'),
    path('oficinas/', HomeOficina.as_view(),name='homeoficinas'),
    path("oficinas/<int:pk>", DetalhesOficina.as_view(),name='detalhesoficinas'),
    ]