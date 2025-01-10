from django.contrib import admin
from .models import livros, usuarios, emprestimos

class usuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'role', 'birthDate', 'phone')
    list_display_links = ('id', 'name')
    list_per_page = 10
    search_fields = ('name', 'email', 'role')
admin.site.register(usuarios, usuariosAdmin)

class livrosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'editora', 'ano_publicacao', 'genero', 'status', 'isbn')
    list_display_links = ('id', 'titulo')
    list_per_page = 10
    search_fields = ('titulo', 'autor', 'editora')
admin.site.register(livros, livrosAdmin)

class emprestimosAdmin(admin.ModelAdmin):
    list_display = ('id', 'livro', 'usuario', 'data_emprestimo', 'data_devolucao', 'status')
    list_display_links = ('id', 'livro')
    list_per_page = 10
    search_fields = ('livro', 'usuario')
admin.site.register(emprestimos, emprestimosAdmin)