from django import forms
from principal.models import *

class ClienteForm(forms.ModelForm):
 
    class Meta:
        model= Cliente
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model= Pedido
        exclude=('valor',)

        widgets = {
            'produto':forms.RadioSelect(),

        }

class ContaForm(forms.ModelForm):
     
    class Meta:
        model= Conta
        fields = '__all__'
       

class AddProdutoForm(forms.ModelForm):
      class Meta:
        model= Produto
        fields = '__all__'
