from django.db import models
from django.core.validators import MinLengthValidator

class livros(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    genero = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=100)
    birthDate = models.DateField()
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name

class emprestimos(models.Model):
    id = models.AutoField(primary_key=True)
    livro = models.ForeignKey(livros, on_delete=models.CASCADE)
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.livro.titulo