from django.db import models


class TipoPosse(models.Model):
    descricao = models.CharField(max_length=256)

    def __str__(self):
        return self.descricao


class TipoOcupacao(models.Model):
    descricao = models.CharField(max_length=256)

    def __str__(self):
        return self.descricao


class TipoRecHidrico(models.Model):
    descricao = models.CharField(max_length=256)

    def __str__(self):
        return self.descricao


class Pessoa(models.Model):
    nome = models.CharField(max_length=256)
    cpf = models.CharField(max_length=11)
    idade = models.IntegerField()
    email = models.CharField(max_length=256)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=256)

    def __str__(self):
        return self.nome + ' - ' + self.cpf


class Imovel(models.Model):
    codigo = models.CharField(max_length=256)
    nome = models.CharField(max_length=256)
    croqui = models.CharField(max_length=256)

    geolocalizacao = models.CharField(max_length=256)
    municipio = models.CharField(max_length=256)
    estado = models.CharField(max_length=2)

    curso_agua = models.CharField(max_length=256)

    area = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    tamanho = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    agriFamiliar = models.BooleanField()

    def __str__(self):
        return self.nome


class Questionario(models.Model):
    data = models.DateField()
    colaborador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='colaborador')

    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    beneficiario = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='beneficiario')

    posse = models.ForeignKey(TipoPosse, on_delete=models.CASCADE)
    sucessao = models.BooleanField()
    participacaoMulher = models.BooleanField()

    # Proporção da área em porcentagem
    lavoutasPermanentes = models.DecimalField(decimal_places=2, max_digits=10, default=0) # Auto gerado pelos objetos de Ocupacao
    lavoutasTemporárias = models.DecimalField(decimal_places=2, max_digits=10, default=0) # Auto gerado pelos objetos de Ocupacao
    pastagens = models.DecimalField(decimal_places=2, max_digits=10, default=0) # Auto gerado pelos objetos de Ocupacao
    silvicultura = models.DecimalField(decimal_places=2, max_digits=10, default=0) # Auto gerado pelos objetos de Ocupacao
    areaNaoAgricola = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    pousio = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    cursosDAgua = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    vegetacaoNativa = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    areasInaproveitaveis = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return self.imovel - self.data


class Ocupacao(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(TipoOcupacao, on_delete=models.CASCADE)
    area = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return self.questionario + ' - ' + self.ocupacao


class RecHidrico(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    recHidrico = models.ForeignKey(TipoRecHidrico, on_delete=models.CASCADE)
    area = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return self.questionario + ' - ' + self.recHidrico


class AreasNaoContiguas(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    identificacaoLocal = models.CharField(max_length=256)
    area = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return self.questionario + ' - ' + self.identificacaoLocal
