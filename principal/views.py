from django.shortcuts import render
from principal.models import *
from principal.forms import *

def index(request):
    pedidos = Pedido.objects.all()
    return render(request,"index.html",{'pedidos':pedidos})

def produtos(request):
    lista = Produto.objects.all()
    context = {'produtos': lista}
    return render (request, 'produtos.html',context)

def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    
    return render (request, 'cadastro_cliente.html', { 'form' : form})
def carrinho(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PedidoForm()
    
    return render (request, 'carrinho.html', { 'form' : form})

def detalhes (request,id):
    produto = Produto.objects.get(id=id)
    context = {'produto': produto}
    return render (request, 'detalhes.html', context)

def conta(request,id):
    if request.method == 'POST':
        form = ContaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContaForm()
    
    pedido = Pedido.objects.get(id=id)
    context={}
    context['form']=form
    context['valor']=20000
    context['pedido']=pedido
    return render (request, 'conta.html', context)

def addproduto(request):
    if request.method == 'POST':
        form = AddProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddProdutoForm()
    
    return render (request, 'addproduto.html', { 'form' : form})
