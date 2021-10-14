from django.views import View
from .models import Company
from django.http import JsonResponse
from django.db import connection

# Create your views here. //FUNCIONES
class UsuarioListView(View):
    def get(self,request):
        lista = []
        cursor = connection.cursor()
        #cursor.execute("select * from usuario where usuario='opacoticona'")
        cursor.execute("exec [ListarClientes]")        
        usuariolist = Company.objects.all()
        rows=cursor.fetchall()
        filas = []
        for row in rows:                        
             #lista.append(row)
             #fila = {'id':row[0], 'nombre': row[2]}
             fila = {'iIdCliente':row[0], 'sCliente': row[1]}
             filas.append(fila)
        print(lista) 
        return  JsonResponse({'nombres':filas, 'mensaje':'todos los datos ok'})

        #usuariolist = Usuario.objects.all()
        #return JsonResponse(list(usuariolist.values()), safe=False)
        #return JsonResponse(usuariolist.values()), False)


    """def post(self, request):
        #post
    def put(self, request):
        #put
    def delete(self, request):
        #delete"""

    