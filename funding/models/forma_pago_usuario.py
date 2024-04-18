from django.db import models
from .forma_pago import FormaPago
from django.contrib.auth.models import User

class FormaPagoUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    forma_pago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True, null=True)
    fecha_ult_act = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f'{self.usuario} ({self.id})'

    class Meta:
        db_table = 'st_formas_pago_usuarios'
        verbose_name = 'Forma de Pago por Usuario'
        verbose_name_plural = 'Formas de Pago por Usuario'