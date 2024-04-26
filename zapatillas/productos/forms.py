from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['modelo', 'color', 'talla_minima', 'talla_maxima', 'marca', 'precio', 'descripcion', 'pais_de_origen', 'condicion', 'disciplina', 'material_del_forro', 'genero', 'material_principal']


