from django.db import models

class empregar(models.Model):
    empresa = models.CharField(max_length=200, verbose_name="Nome da empresa")
    titulo = models.CharField(max_length=200, verbose_name="Area de atuacao")
    Descricao = models.CharField(max_length=500)
    responsabilidades = models.TextField()
    requisitos = models.TextField()
    processo_candidatura = models.EmailField(blank=True, null=True)
    data_de_publicacao = models.DateField(auto_now_add=True)
    data_limite = models.DateField()
    imagem = models.ImageField(upload_to='Imagem_vaga', blank=True, null=True)
    localizacao = models.CharField(max_length=100, blank=True, null= True)
    site = models.URLField(blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.titulo} - {self.empresa}"

class Cursar(models.Model):
    instituicao = models.CharField(max_length=200)
    Nome_curso = models.CharField(max_length=200, verbose_name = "Nome do curso")
    localizacao = models.CharField(blank= True, null = True)
    email_contato = models.EmailField(blank = True, null = True)
    site = models.URLField(blank= True, null=True)
    imagem = models.ImageField(upload_to='Imagem_curso', blank=True, null = True)
    Descricao_curso = models.TextField()
    requisitos = models.TextField()
    inscricao = models.IntegerField(verbose_name="Valor da inscricao")
    mensalidade = models.IntegerField(verbose_name="Valor da mensalidade")
    inicio_inscricao = models.DateField(auto_now_add=True)
    limite_inscricao = models.DateField(verbose_name="data limite de candidatura")
    Duracao = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Duracao do Curso")
    palavrsa_chave = models.TextField("Palavras chaves (separadas por virgula)")
    banner = models.ImageField(upload_to = 'banner', blank = True, null = True)
    def __str__(self):
        return f"{self.Nome_curso}"
    """© 2025 Cleiton Ernesto Cumbane. Todos os direitos reservados.
   Este código faz parte do projeto SpotDjob.
   Uso não autorizado, cópia ou distribuição são proibidos sem permissão.
   """
    
 
