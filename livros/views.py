from .models import livros, usuarios, emprestimos
from .serializers import Livros_Serializer, Usuarios_Serializer, Emprestimos_Serializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class LivrosViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = livros.objects.all()
    serializer_class = Livros_Serializer

class UsuariosViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Usuarios_Serializer

    def get_queryset(self):
        queryset = usuarios.objects.all()
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(name=name)

        return queryset

class EmprestimosViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = emprestimos.objects.all()
    serializer_class = Emprestimos_Serializer

# class Emprestimos_List(generics.ListAPIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         queryset = emprestimos.objects.filter(livro_id = self.kwargs['pk'])
#         return queryset

#     serializer_class = Emprestimos_List_Serializer

#     def get_status(self, obj):
#         return obj.get_status_display()
# class Emprestimos_List(generics.ListAPIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         queryset = emprestimos.objects.filter(usuario_id = self.kwargs['pk'])
#         return queryset

#     serializer_class = Emprestimos_List_Serializer

#     def get_period(self, obj):
#         return obj.get_period_display()