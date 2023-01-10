from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.TextField()
    valor = models.DecimalField('Preço do produto',max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/',blank=True, null=True, max_length=250)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=80)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome

class Pedido(models.Model):
    mesa = models.CharField(max_length=5)
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    observacao = models.TextField(blank=True, null=True)
    quantidade = models.IntegerField()
    valor = models.DecimalField('Valor do pedido',max_digits=8, decimal_places=2,blank=True)
    
    def save(self, *args, **kwargs):
        self.valor = self.produto.valor * self.quantidade 
        super(Pedido, self).save(*args, **kwargs) 

    def __str__(self):
        return self.mesa
    
class Conta(models.Model):
    pagamento = models.CharField('Informe a forma de pagamento', max_length=80)
 
        





