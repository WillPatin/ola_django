from django.urls import path
from django.http import HttpResponse
from .views import PessoaCreateView, PessoaListView, PessoaUpdateView

def oiDjango(request):
    return HttpResponse('Ola primeiroAPP')

urlpatterns = [
     path('ola/', oiDjango),
     path('cadastrar_pessoa/', PessoaCreateView.as_view(), name='cadastrar_pessoa'),
     path('listar_pessoa/', PessoaListView.as_view(), name='lista_pessoas'),
     path('editar_pessoa/<int:pk>/', PessoaUpdateView.as_view(), name='editar_pessoa'),
]
