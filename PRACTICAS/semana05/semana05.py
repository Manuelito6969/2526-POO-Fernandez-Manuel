"""
Ejercicio: Simulación de un Sistema Bancario en Python usando Programación Orientada a Objetos (POO)

Descripción:
Este programa simula un sistema bancario básico que permite gestionar clientes, cajeros y cuentas bancarias.
Se pueden realizar depósitos, retiros y calcular el interés de cuentas de ahorro. El diseño utiliza herencia,
atributos de diferentes tipos de datos (str, int, float, bool) y buenas prácticas de codificación.
"""

# ---------- Clases ----------

class Persona:
    def __init__(self, nombre: str, cedula: str, edad: int):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad  # tipo int


class Cliente(Persona):
    def __init__(self, nombre: str, cedula: str, edad: int, es_vip: bool = False):
        super().__init__(nombre, cedula, edad)
        self.es_vip = es_vip  # tipo boolean
        self.cuentas = []     # lista de cuentas asociadas

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)


class Cajero(Persona):
    def __init__(self, nombre: str, cedula: str, edad: int):
        super().__init__(nombre, cedula, edad)

    def procesar_deposito(self, cuenta, monto):
        print(f"Cajero {self.nombre} procesando depósito...")
        cuenta.depositar(monto)

    def procesar_retiro(self, cuenta, monto):
        print(f"Cajero {self.nombre} procesando retiro...")
        cuenta.retirar(monto)


class Cuenta:
    def __init__(self, numero: str, saldo_inicial: float = 0.0, activa: bool = True):
        self.numero = numero
        self.saldo = saldo_inicial
        self.activa = activa         # tipo bool
        self.transacciones = 0       # tipo int

    def depositar(self, monto: float):
        if not self.activa:
            print("La cuenta está inactiva. No se puede depositar.")
            return
        if monto > 0:
            self.saldo += monto
            self.transacciones += 1
            print(f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto: float):
        if not self.activa:
            print("La cuenta está inactiva. No se puede retirar.")
            return
        if monto <= self.saldo:
            self.saldo -= monto
            self.transacciones += 1
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("Fondos insuficientes.")


class CuentaAhorro(Cuenta):
    def __init__(self, numero: str, saldo_inicial: float = 0.0, tasa_interes: float = 0.03):
        super().__init__(numero, saldo_inicial)
        self.tasa_interes = tasa_interes  # tipo float

    def calcular_interes_anual(self) -> float:
        """
        Calcula el interés generado en un año sobre el saldo actual.
        """
        return self.saldo * self.tasa_interes


class CuentaCorriente(Cuenta):
    def __init__(self, numero: str, saldo_inicial: float = 0.0, limite_sobregiro: float = 100.0):
        super().__init__(numero, saldo_inicial)
        self.limite_sobregiro = limite_sobregiro  # tipo float

    def retirar(self, monto: float):
        if not self.activa:
            print("La cuenta está inactiva. No se puede retirar.")
            return
        if monto <= self.saldo + self.limite_sobregiro:
            self.saldo -= monto
            self.transacciones += 1
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("Fondos insuficientes, incluso con sobregiro.")


# ---------- Simulación del sistema ----------

# Crear cliente
cliente1 = Cliente("Ana Morales", "1102354789", edad=35, es_vip=True)

# Crear cuentas
cuenta_ahorro = CuentaAhorro("AH003", 1000.0, tasa_interes=0.04)
cuenta_corriente = CuentaCorriente("CC003", 300.0)

# Asociar cuentas al cliente
cliente1.agregar_cuenta(cuenta_ahorro)
cliente1.agregar_cuenta(cuenta_corriente)

# Crear cajero
cajero1 = Cajero("Pedro Ruiz", "1109988776", edad=40)

# Operaciones
print("\n--- Depósito en cuenta de ahorro ---")
cajero1.procesar_deposito(cuenta_ahorro, 200)

print("\n--- Retiro en cuenta corriente ---")
cajero1.procesar_retiro(cuenta_corriente, 350)

print("\n--- Cálculo de interés anual en cuenta de ahorro ---")
interes = cuenta_ahorro.calcular_interes_anual()
print(f"Interés anual estimado: ${interes:.2f}")

# Mostrar resumen de cuentas
print("\n--- Resumen de cuentas del cliente ---")
for cuenta in cliente1.cuentas:
    estado = "Activa" if cuenta.activa else "Inactiva"
    print(f"Cuenta {cuenta.numero}:")
    print(f"  Saldo: ${cuenta.saldo:.2f}")
    print(f"  Transacciones: {cuenta.transacciones}")
    print(f"  Estado: {estado}")
    if isinstance(cuenta, CuentaAhorro):
        print(f"  Tasa de interés: {cuenta.tasa_interes * 100}%")
