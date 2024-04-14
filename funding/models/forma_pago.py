from django.db import models
from django.contrib.auth.models import User

class FormaPago(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes/', null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True, null=True)
    fecha_ult_act = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'st_formas_pago'
        verbose_name = 'Forma de Pago'
        verbose_name_plural = 'Formas de Pago'