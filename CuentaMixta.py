from CUENTAAHORRO import CUENTAAHORRO
from CUENTACORRIENTE import CUENTACORRIENTE


class CuentaMixta(CUENTAAHORRO, CUENTACORRIENTE):
    def __init__(self, numero, nombre_propietario, saldo, interes, tieneChequera, limite:float=None, bono:float=None):
        CuentaAhorros.__init__(self, numero, nombre_propietario, saldo, interes)
        CuentaCorriente.__init__(self, numero, nombre_propietario, saldo, tieneChequera)
        self._limite = limite
        self._bono = bono
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, cantidad):
        self._limite = cantidad

    @property
    def bono(self):
        return self._bono

    @bono.setter
    def bono(self, cantidad):
        self._bono = cantidad

    #def __str__(self):
     #   return f"Cuenta mixta - Saldo: {self.saldo}, Tasa de interés: {self.tasa_interes}, Sobregiro: {self.sobregiro}, Límite: {self.limite}, Bono: {self.bono}"

#EJEMPLO DE USO
cuenta_mixta = CuentaMixta(numero='2234483', nombre_propietario='Nataly Garcia',saldo=1000, interes=0.02, tieneChequera=500, limite=2000, bono=100)
print("Saldo inicial de la cuenta mixta:", cuenta_mixta.saldo)
print("Límite de la cuenta mixta:", cuenta_mixta._limite)
print("Bono de la cuenta mixta:", cuenta_mixta._bono)

cuenta_mixta.credito(500)
print("Saldo después del depósito:", cuenta_mixta.saldo)

cuenta_mixta.debito(1200)
print("Saldo después del retiro:", cuenta_mixta.saldo)
