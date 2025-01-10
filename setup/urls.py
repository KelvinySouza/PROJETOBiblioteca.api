from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from livros.views import LivrosViewSet, UsuariosViewSet, EmprestimosViewSet

router = routers.DefaultRouter()
router.register('livros', LivrosViewSet, basename='livros')
router.register('usuarios', UsuariosViewSet, basename='usuarios')
router.register('emprestimos', EmprestimosViewSet, basename='emprestimos')


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include(router.urls)),

]
