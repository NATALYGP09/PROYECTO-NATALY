from CUENTA import CUENTA

#NATALY GARCIA PIGUAVE
class CUENTACORRIENTE(CUENTA):
    def __init__(self, numero, nombrePropietario, saldo, TieneChequera: bool = None):
        super().__init__(numero, nombrePropietario, saldo)
        self._TieneChequera = TieneChequera

    @property
    def TieneChequera(self):
        return self._TieneChequera

    @TieneChequera.setter
    def TieneChequera(self, tiene_chequera):
        self._TieneChequera = tiene_chequera

    def credito(self, cantidad):
        self.saldo += cantidad

    def debito(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"Saldo de la cuenta corriente {self.numero}: ${self.saldo}")

    def pagar_cheque(self, cantidad):
        if self.TieneChequera:
            self.debito(cantidad)
            print(f"Se pagó un cheque por ${cantidad}")
        else:
            print("Esta cuenta corriente no tiene chequera")

# Ejemplo
#cuenta_pru = CuentaCorriente("23409", "Maria Eujenia", 7895.00, True)
#cuenta_pru.credito(898.00)
#cuenta_pru.debito(795.00)
#cuenta_pru.mostrar_saldo()
#cuenta_pru.pagar_cheque(401.00)
#cuenta_pru.mostrar_saldo()