import os
import django

# Configura el entorno para Django antes de importar modelos
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zapatillas.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

usuarios_predefinidos = [
    ('maria@a.com', 'u1'),
    ('juan@b.com', 'u2'),
    ('jose@c.com', 'u3'),
    ('nico@d.com', 'u4'),
    ('isabel@e.com', 'u5'),
    ('isis@f.com', 'u6'),
    ('mary@g.com', 'u7'),
    ('ali@h.com', 'u8'),
    ('angel@i.com', 'u9'),
    ('andy@j.com', 'u10'),
]

for email, password in usuarios_predefinidos:
    if not User.objects.filter(username=email).exists():
        User.objects.create(username=email, email=email, password=make_password(password))

print("Usuarios creados exitosamente")