
from usuarios.models import PerfilUsuario

def perfil_context(request):
    perfil_usuario = None
    if request.user.is_authenticated:
        try:
            perfil_usuario = request.user.perfilusuario
        except PerfilUsuario.DoesNotExist:
           
            perfil_usuario = PerfilUsuario.objects.create(user=request.user)
    return {'perfil_usuario': perfil_usuario}