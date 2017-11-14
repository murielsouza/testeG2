from django.db import models

class Horarios(models.Model): #classe configurações
    h_entrada = models.TimeField(blank=True, null=True)
    h_saida = models.TimeField(blank=True, null=True)
    #funcionario = models.ForeignKey(Funcionario, null=True, blank=False)

    def __str__(self):
        return str(self.h_entrada) + " - " + str(self.h_saida)

class Funcionario(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models. CharField(max_length=14)
    horarios = models.ManyToManyField(Horarios, blank=True, related_name='horarios')

    def __str__(self):
        return self.nome

class Frequencia(models.Model):
    TIPO_CHOICES = (
        ('entrada', 'ENTRADA'),
        ('saida', 'SAIDA'),
    )
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES, blank=False, null=False)
    hora = models.TimeField(blank=True, null=True)
    ip = models.CharField(max_length=15)
    status = models.BooleanField("Consistência da frequência!?",default=False) #True: Consistente, False: Incosistente
    funcionario = models.ForeignKey(Funcionario, null=True, blank=False)

    def __str__(self):
        return self.funcionario.nome + ": " + self.tipo + " - " + str(self.hora)

class Justificativa(models.Model):
    motivo = models.CharField(max_length=35)
    descricao = models.TextField()
    boss = models.ForeignKey(Funcionario, null = True, blank = False)
    freq_inconsistencia = models.ForeignKey(Frequencia, null = True, blank = False)

    def __str__(self):
        return self.motivo
