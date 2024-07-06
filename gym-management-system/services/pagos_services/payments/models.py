# payments/models.py

from django.db import models

class Payment(models.Model):
    iddepago = models.AutoField(primary_key=True)
    idperson = models.IntegerField()
    pago = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()

    def __str__(self):
        return f"Payment {self.iddepago} - Person {self.idperson}"
