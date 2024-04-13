from django.contrib import admin

# Register your models here.
from funding.models import Categoria, Campania, FormaPago, Beneficiario, FormaPagoUsuario

admin.site.site_header = 'Administrador de CrowdFunding'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'fecha_registro', 'fecha_ult_act')
    
@admin.register(Campania)
class CampaniaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'nombre', 
        'descripcion',
        'foto', 
        'monto_x_recaudar', 
        'monto_recaudado',
        'fecha_inicio',
        'fecha_cierre',
        'fecha_registro',
        'fecha_ult_act'
    )
    
@admin.register(FormaPago)
class FormaPagoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'fecha_registro',
        'fecha_ult_act'
    )
    
@admin.register(Beneficiario)
class FormaPagousuarioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre', 
        'fecha_nacimiento',
        'pais',
        'ciudad',
        'email',
        'telefono',
        'fecha_registro',
        'fecha_ult_act' 
    )
    
@admin.register(FormaPagoUsuario)
class FormaPagoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario',
        'forma_pago',
        'fecha_registro',
        'fecha_ult_act'
    )