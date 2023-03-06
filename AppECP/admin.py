from django.contrib import admin
from .models import Profile, Categorias, Producto, ImageProducto #Carrito, Carrito_item
from .forms import ProductoFormulario

# Register your models here.


class ImageProductoAdmin(admin.TabularInline):
    model = ImageProducto

class ProductoAdministration(admin.ModelAdmin):
    form = ProductoFormulario
    inlines = [
        ImageProductoAdmin
    ]


admin.site.register(Profile)
admin.site.register(Categorias)
admin.site.register(Producto)
#admin.site.register(Carrito_item)
#admin.site.register(Carrito)