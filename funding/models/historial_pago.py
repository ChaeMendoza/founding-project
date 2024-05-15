from django.db import models
from .campania import Campania
from django.contrib.auth.models import User

class HistorialPago(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    campania = models.ForeignKey(Campania, on_delete=models.CASCADE, null=True)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True, null=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.usuario} (${self.valor})'
    
    class Meta:
        db_table = 'st_historial_pagos'
        verbose_name = 'Historial de Pago'
        verbose_name_plural = 'Historial de Pagos'