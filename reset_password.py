import sys
import os
import django

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_base.settings")
django.setup()

from django.contrib.auth import get_user_model

# Obtener el modelo de usuario personalizado
User = get_user_model()

# Validar argumentos
if len(sys.argv) != 3:
    print("Uso: python reset_password.py <usuario> <nueva_contraseña>")
    sys.exit(1)

username = sys.argv[1]
new_password = sys.argv[2]

try:
    user = User.objects.get(username=username)
    user.set_password(new_password)
    user.save()
    print(f"✅ Contraseña actualizada correctamente para el usuario: {username}")
except User.DoesNotExist:
    print(f"❌ El usuario '{username}' no existe en la base de datos.")
