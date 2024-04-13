from django.db import models

class Beneficiario(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'st_beneficiarios'
        verbose_name = 'Beneficiario'
        verbose_name_plural = 'Beneficiarios'