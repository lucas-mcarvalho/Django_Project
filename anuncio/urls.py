from django.urls import path,include
from anuncio.views import ListarAnuncios, EditarAnuncios, CriarAnuncios, DeletarAnuncios
urlpatterns = [
    path('listar-anuncios/', ListarAnuncios.as_view(), name='listar-anuncios'),
    # Atenção aos nomes aqui embaixo, devem estar no SINGULAR:
    path('editar/<int:pk>/', EditarAnuncios.as_view(), name='editar-anuncio'),
    path('novo/', CriarAnuncios.as_view(), name='criar-anuncio'),
    path('deletar/<int:pk>/', DeletarAnuncios.as_view(), name='deletar-anuncio'),
]