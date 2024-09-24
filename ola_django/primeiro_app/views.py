from django.shortcuts import render
from django.views.generic import CreateView
from .models import Pessoa
from .forms import PessoaForm

# Create your views here.
#criação tela de cadastro pessoa
class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template = 'cadastrar_pessoa.html'
