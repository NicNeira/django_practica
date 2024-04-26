from django.db import models

# Define tus opciones de colores, marcas y otros campos aquí
COLOR_CHOICES = [
    ('blanco', 'Blanco'),
    ('negro', 'Negro'),
    ('azul', 'Azul'),
    ('rojo', 'Rojo'),  # Ejemplo de un color adicional
    ('verde', 'Verde'),  # Ejemplo de un color adicional
    ('amarillo', 'Amarillo'),  # Ejemplo de un color adicional
    ('gris', 'Gris'),  # Ejemplo de un color adicional
]

MARCA_CHOICES = [
    ('nike', 'Nike'),
    ('adidas', 'Adidas'),
    ('puma', 'Puma'),
    ('asics', 'Asics'),  # Ejemplo de una marca adicional
    ('under armour', 'Under Armour'),  # Ejemplo de una marca adicional
    ('new balance', 'New Balance'),  # Ejemplo de una marca adicional
    ('reebok', 'Reebok'),  # Ejemplo de una marca adicional
]

# Agrega más opciones para otros campos si es necesario

class Zapatilla(models.Model):
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    talla_minima = models.FloatField()
    talla_maxima = models.FloatField()
    marca = models.CharField(max_length=50, choices=MARCA_CHOICES)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    pais_de_origen = models.CharField(max_length=100)  
    condicion = models.CharField(max_length=100)  
    disciplina = models.CharField(max_length=100)  
    material_del_forro = models.CharField(max_length=100)  
    genero = models.CharField(max_length=100)  
    material_principal = models.CharField(max_length=100)  

    def __str__(self):
        return f"{self.modelo} - {self.marca}"




