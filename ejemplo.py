from CUENTAAHORRO import CUENTAAHORRO
from CUENTACORRIENTE import CUENTACORRIENTE
#Nataly garcia piguave

class Test(CUENTAAHORRO, CUENTACORRIENTE):
    def __init__(self, numero, nombrePropietario, saldo, interes, TieneChequera):
        CUENTAAHORRO.__init__(self, numero, nombrePropietario, saldo, interes)
        CUENTACORRIENTE.__init__(self, numero, nombrePropietario, saldo, TieneChequera)

# Ejemplo
cuenta_pru = Test("20040709", "MENDOZA DAYANA", 4891.72, 7.9, True)

# Acceder a propiedades y métodos de ambas clases base
print("Saldo de la cuenta de ahorros:")
print(cuenta_pru.saldo)
print("Tiene chequera en la cuenta corriente:")
print(cuenta_pru.TieneChequera)

# Realizar transacciones
cuenta_pru.credito(456.0)
cuenta_pru.debito(80.0)
cuenta_pru.pagar_cheque(120.0)

# Mostrar saldos después de las transacciones
print("Saldo después de las transacciones:")
print(cuenta_pru.saldo)