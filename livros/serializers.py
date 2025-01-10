from rest_framework import serializers
from .models import livros, usuarios, emprestimos


class Livros_Serializer(serializers.ModelSerializer):
    class Meta:
        model = livros
        fields = ['id', 'titulo', 'autor', 'editora', 'ano_publicacao', 'genero', 'status', 'isbn']

class Usuarios_Serializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = ['id', 'name', 'email', 'role', 'birthDate', 'phone']

class Emprestimos_Serializer(serializers.ModelSerializer):
    class Meta:
        model = emprestimos
        fields = ['id', 'usuario', 'livro', 'data_emprestimo', 'data_devolucao']

