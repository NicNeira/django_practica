from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"Usuario: {self.username}"

    def check_credentials(self, username, password):
        return self.username == username and self.password == password


# usuarios_predefinidos = [
#     Usuario('maria@a.com', 'u1'),
#     Usuario('juan@b.com', 'u2'),
#     Usuario('jose@c.com', 'u3'),
#     Usuario('nico@d.com', 'u4'),
#     Usuario('isabel@e.com', 'u5'),
#     Usuario('isis@f.com', 'u6'),
#     Usuario('mary@g.com', 'u7'),
#     Usuario('ali@h.com', 'u8'),
#     Usuario('angel@i.com', 'u9'),
#     Usuario('andy@j.com', 'u10'),
# ]

# def authenticate_user(username, password):
#     for usuario in usuarios_predefinidos:
#         if usuario.check_credentials(username, password):
#             return True
#     return False

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Utiliza la función authenticate de Django para verificar las credenciales
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si las credenciales son correctas, inicia sesión con el usuario
            login(request, user)
            return redirect('index')
        else:
            # Si las credenciales son incorrectas, muestra una página de error
            return render(request, 'error.html', {'message': 'Invalid login details'})
    
    return render(request, 'login.html')


from django.shortcuts import render, redirect
from .models import Zapatilla

def index(request):
    # Esta línea consulta la base de datos y obtiene todas las instancias del modelo Zapatilla
    zapatillas = Zapatilla.objects.all()
    
    # Luego, pasas la lista de zapatillas a la plantilla
    return render(request, 'productos/index.html', {'productos': zapatillas})



    # Lista de zapatillas estática
    return render(request, 'productos/index.html', {'productos': zapatillas})

def agregar_producto(request):
    if request.method == "POST":
        modelo = request.POST['modelo']
        color = request.POST['color']
        talla_minima = request.POST['talla_minima']
        talla_maxima = request.POST['talla_maxima']
        marca = request.POST['marca']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        pais_de_origen = request.POST['pais_de_origen']
        condicion = request.POST['condicion']
        disciplina = request.POST['disciplina']
        material_del_forro = request.POST['material_del_forro']
        genero = request.POST['genero']
        material_principal = request.POST['material_principal']

        if modelo and color and talla_minima and talla_maxima and marca and precio and descripcion:
            Zapatilla.objects.create(
                modelo=modelo,
                color=color,
                talla_minima=talla_minima,
                talla_maxima=talla_maxima,
                marca=marca,
                precio=precio,
                descripcion=descripcion,
                pais_de_origen=pais_de_origen,
                condicion=condicion,
                disciplina=disciplina,
                material_del_forro=material_del_forro,
                genero=genero,
                material_principal=material_principal
            )
            return redirect('index')
        else:
            mensaje = "Error: Todos los campos son obligatorios"
            return render(request, 'productos/agregar_producto.html', {'mensaje': mensaje})

    return render(request, 'productos/agregar_producto.html')

def editar_producto(request, id):
    producto = get_object_or_404(Zapatilla, pk=id)

    if request.method == "POST":
        modelo = request.POST['modelo']
        color = request.POST['color']
        talla_minima = request.POST['talla_minima']
        talla_maxima = request.POST['talla_maxima']
        marca = request.POST['marca']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        pais_de_origen = request.POST['pais_de_origen']
        condicion = request.POST['condicion']
        disciplina = request.POST['disciplina']
        material_del_forro = request.POST['material_del_forro']
        genero = request.POST['genero']
        material_principal = request.POST['material_principal']

        if modelo and color and talla_minima and talla_maxima and marca and precio and descripcion:
            producto.modelo = modelo
            producto.color = color
            producto.talla_minima = talla_minima
            producto.talla_maxima = talla_maxima
            producto.marca = marca
            producto.precio = precio
            producto.descripcion = descripcion
            producto.pais_de_origen = pais_de_origen
            producto.condicion = condicion
            producto.disciplina = disciplina
            producto.material_del_forro = material_del_forro
            producto.genero = genero
            producto.material_principal = material_principal
            producto.save()
            return redirect('index')
        else:
            mensaje = "Error: Todos los campos son obligatorios"
            return render(request, 'productos/editar_producto.html', {'producto': producto, 'mensaje': mensaje})

    return render(request, 'productos/editar_producto.html', {'producto': producto})

def eliminar_producto(request, pk):
    producto = Zapatilla.objects.get(pk=pk)
    producto.delete()
    return redirect('index')


