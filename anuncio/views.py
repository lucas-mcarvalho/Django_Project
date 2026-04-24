from django.urls import reverse_lazy

# Adicionamos o UpdateView aqui e juntamos as importações do generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from anuncio.models import Anuncio
from anuncio.forms import AnuncioForm


class ListarAnuncios(ListView):
    model = Anuncio
    context_object_name = "anuncios"
    template_name = "ListarAnuncios.html"

    def get_queryset(self):
        pesquisa = self.request.GET.get("pesquisa", None)
        queryset = Anuncio.objects.all()
        if pesquisa:
            queryset = queryset.filter(titulo__icontains=pesquisa)
        return queryset


class EditarAnuncios(LoginRequiredMixin, UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = "editar_anuncio.html"
    success_url = reverse_lazy("listar-anuncios")


class CriarAnuncios(LoginRequiredMixin, CreateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = "criar_anuncio.html"
    success_url = reverse_lazy("listar-anuncios")


class DeletarAnuncios(LoginRequiredMixin, DeleteView):
    model = Anuncio
    template_name = "deletar_anuncio.html"
    success_url = reverse_lazy("listar-anuncios")

