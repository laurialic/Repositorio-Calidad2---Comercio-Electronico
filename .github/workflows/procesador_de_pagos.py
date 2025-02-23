## procesador_de_pagos.py
class ProcesadorDePagos:
    def procesar_pago(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo.")
        return True
