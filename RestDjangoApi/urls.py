from django.urls import path
from .views import UsuarioListView

urlpatterns = [
    path('usuario/', UsuarioListView.as_view(), name='usuario_list'),

]