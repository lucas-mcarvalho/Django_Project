from django.shortcuts import render
from django.views import View
from django.views.generic import DeleteView, ListView, UpdateView
from veiculo.models import Veiculo
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView
from veiculo.forms import FormularioVeiculo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListarVeiculos(LoginRequiredMixin,ListView):
    """
    View para listar os veículos cadastrados.
    """
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'listar.html'
    def get_queryset(self,**kwargs):
        pesquisa = self.request.GET.get('pesquisa',None)
        queryset = Veiculo.objects.all()
        if pesquisa is not None:
            queryset = queryset.filter(modelo__icontains=pesquisa)
        return queryset

class FotoVeiculo(View):
    def get(self,request,arquivo):
            try:
             Veiculo = Veiculo.objects.get(foto = 'veiculos/fotos{}'.format(arquivo))
             return FileResponse(veiculo.foto)
            except ObjectDoesNotExist:
                raise Http404("Foto não encontrada ou acesso não autorizado.")
            except Exception as exception:
                raise exception
    
class CriarVeiculos(LoginRequiredMixin,CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'novo.html'
    success_url = reverse_lazy('listar-veiculos')

class EditarVeiculos(LoginRequiredMixin,UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'editar.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculos(LoginRequiredMixin,DeleteView):
    model = Veiculo
    template_name = 'deletar.html'
    success_url = reverse_lazy('listar-veiculos')