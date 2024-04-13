from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'st_categorias'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'