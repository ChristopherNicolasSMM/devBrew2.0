from django.db import models

class Malte(models.Model):
    nome = models.CharField(max_length=255)
    origem = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    quantidade_max = models.IntegerField()
    cor = models.IntegerField()
    usar_mostura = models.BooleanField()
    usar_fervura = models.BooleanField()
    nao_fermentavel = models.BooleanField()
    potencial_sg = models.FloatField()
    aproveitamento = models.FloatField()
    poder_diastatico = models.FloatField()
    proteina = models.FloatField()
    extrato_ibu = models.FloatField()
    notas = models.TextField(null=True, blank=True)
    ilustracao = models.CharField(max_length=255, null=True, blank=True)
    preco = models.FloatField()

    def __str__(self):
        return self.nome

