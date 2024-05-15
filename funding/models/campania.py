from django.db import models
from .categoria import Categoria
from .beneficiario import Beneficiario

class Campania(models.Model):
    categorias = models.ManyToManyField(Categoria, related_name='campanias')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='imagenes/')
    beneficiario = models.OneToOneField(Beneficiario, on_delete=models.CASCADE, null=True)
    monto_x_recaudar = models.DecimalField(max_digits=15, decimal_places=2)
    monto_recaudado = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_cierre = models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(null=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'st_campanias'
        verbose_name = 'Campaña'
        verbose_name_plural = 'Campañas'