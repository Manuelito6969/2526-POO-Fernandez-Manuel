class Empleado:
    """Representa a un empleado individual."""

    def __init__(self, nombre, id_empleado, cargo):
        """Inicializa un empleado con nombre, ID y cargo."""
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.cargo = cargo

    def __str__(self):
        """Devuelve una representación en cadena del empleado."""
        return f"{self.nombre} (ID: {self.id_empleado}) - {self.cargo}"


class Departamento:
    """Representa un departamento dentro de la empresa."""

    def __init__(self, nombre):
        """Inicializa un departamento con un nombre."""
        self.nombre = nombre
        self.empleados = []  # Lista para almacenar objetos Empleado

    def agregar_empleado(self, empleado):
        """Añade un objeto Empleado a este departamento."""
        if isinstance(empleado, Empleado):
            self.empleados.append(empleado)
            print(f"-> {empleado.nombre} ha sido añadido a {self.nombre}.")

    def listar_empleados(self):
        """Muestra todos los empleados del departamento."""
        nombres_empleados = [e.nombre for e in self.empleados]
        if nombres_empleados:
            return f"Empleados en {self.nombre}: {', '.join(nombres_empleados)}"
        return f"El departamento de {self.nombre} no tiene empleados."


class Empresa:
    """Representa la empresa que contiene varios departamentos."""

    def __init__(self, nombre):
        """Inicializa la empresa con un nombre."""
        self.nombre = nombre
        self.departamentos = {}  # Diccionario para almacenar objetos Departamento

    def agregar_departamento(self, departamento):
        """Añade un objeto Departamento a la empresa."""
        if isinstance(departamento, Departamento):
            self.departamentos[departamento.nombre] = departamento
            print(f"**{self.nombre}**: Departamento de {departamento.nombre} creado.")

    def obtener_informe(self):
        """Genera un informe que lista todos los departamentos y sus empleados."""
        print(f"\n--- Informe de Estructura de {self.nombre} ---")
        if not self.departamentos:
            print("No hay departamentos establecidos.")
            return

        # Itera sobre los departamentos para generar el informe
        for nombre_depto, depto in self.departamentos.items():
            print(f"### {depto.nombre} ###")
            print(depto.listar_empleados())
            print("-" * 20)


# --- Ejecución y Prueba ---

# 1. Creación de la Empresa
mi_empresa = Empresa("Tech Solutions S.A.")

# 2. Creación de Departamentos
depto_desarrollo = Departamento("Desarrollo")
depto_rrhh = Departamento("Recursos Humanos")

# 3. Creación de Empleados
empleado1 = Empleado("Andrés Pérez", 101, "Desarrollador Senior")
empleado2 = Empleado("Carla Gómez", 102, "Analista de RRHH")
empleado3 = Empleado("Luis Soto", 103, "Diseñador UX")

# 4. Configuración de la Empresa (Agregación)
mi_empresa.agregar_departamento(depto_desarrollo)
mi_empresa.agregar_departamento(depto_rrhh)

# 5. Asignación de Empleados a Departamentos (Agregación/Composición)
print("\n--- Asignación de Empleados ---")
depto_desarrollo.agregar_empleado(empleado1)
depto_desarrollo.agregar_empleado(empleado3)
depto_rrhh.agregar_empleado(empleado2)

# 6. Generar el Informe Final
mi_empresa.obtener_informe()

print("\n--- Detalle del Empleado 1 ---")
print(empleado1)