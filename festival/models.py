from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Palco(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to="palcos/", null=True, blank=True)
    # Ponto 6 - Novo campo de acessibilidade
    acessibilidade_mobilidade_reduzida = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Dia(models.Model):
    data = models.DateField()
    cor = models.CharField(max_length=20, default="#000000")

    class Meta:
        # Ponto 1 - Ordenação crescente por data
        ordering = ['data']

    def __str__(self):
        return str(self.data)

class Concerto(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name="concertos")
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name="concertos")
    hora = models.TimeField()
    palco = models.ForeignKey(Palco, on_delete=models.CASCADE, related_name="concertos")

    class Meta:
        # Ponto 1 - Ordenação por data e hora
        unique_together = (("dia", "palco", "hora"),)
        ordering = ["dia__data", "hora"]

    def __str__(self):
        return f"{self.banda} - {self.dia}"