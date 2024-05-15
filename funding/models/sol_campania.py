from django.db import models
from .categoria import Categoria

class SolCampania(models.Model):
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='imagenes/')
    beneficiario = models.CharField(max_length=100)
    email=models.CharField(max_length=100,null=True)
    monto_x_recaudar = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(null=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'st_solCampania'
        verbose_name = 'SolicitudCampania'
        verbose_name_plural = 'SolicitudCampanias'