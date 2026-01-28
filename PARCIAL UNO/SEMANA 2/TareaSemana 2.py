# ============================================
#     Clase base: Persona
# ============================================

# --------------------------------------------
# 1. ABSTRACCIÓN (Aplicada en la clase Persona)
# --------------------------------------------
# La abstracción se usa para representar únicamente lo esencial
# de una persona. En este ejemplo, la clase Persona incluye solo
# los atributos básicos que definen a cualquier individuo:
# nombre, apellido, género y edad.
#
# La abstracción permite que esta clase sirva como modelo general
# para otras clases más específicas (como Estudiante o Docente),
# ocultando detalles innecesarios y enfocándose en lo importante.
# --------------------------------------------

class Persona:
    def __init__(self, nombre, apellido, genero, edad):
        # =====================================================
        # 2. ENCAPSULAMIENTO (Protección de los datos)
        # -----------------------------------------------------
        # Los atributos están protegidos usando un guion bajo,
        # lo que indica que no deben ser modificados directamente.
        #
        # Además, se utilizan métodos getters y setters para
        # controlar el acceso a estos datos. Esto permite:
        # Validar valores antes de asignarlos
        # Proteger la integridad de la información
        # Evitar cambios directos no controlados
        #
        # =====================================================
        self._nombre = nombre
        self._apellido = apellido
        self._genero = genero
        self._edad = edad

    # -------- MeTODO DE ABSTRACCIÓN --------
    def mostrar_info(self):
        return f"{self._nombre} {self._apellido} ({self._genero}), {self._edad} años"

    # -------- MÉTODOS DE ENCAPSULAMIENTO --------
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 1:
            self._nombre = nuevo_nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad


# ============================================
#     HERENCIA: Estudiante y Docente
# ============================================

# ---------------------------------------------------------
# 3. HERENCIA (Estudiante y Docente heredan de Persona)
# ---------------------------------------------------------
# La herencia permite crear nuevas clases basadas en una clase
# existente. En este ejemplo:
#
# • Estudiante(Persona)
# • Docente(Persona)
#
# Gracias a la herencia:
# Se reutilizan los atributos nombre, apellido, género, edad
# No es necesario reescribir código repetido
# Se agregan atributos propios: carrera y especialidad
# Se puede expandir comportamiento sin duplicar código
# ---------------------------------------------------------

class Estudiante(Persona):
    def __init__(self, nombre, apellido, genero, edad, carrera):
        # Llama al constructor de Persona
        super().__init__(nombre, apellido, genero, edad)
        self.carrera = carrera

    # ---------------------------------------------
    # 4. POLIMORFISMO: metodo mostrar_info() redefinido
    # ---------------------------------------------
    # El polimorfismo permite que el mismo metodo (mostrar_info)
    # funcione diferente según el tipo de objeto.
    #
    # Aquí, Estudiante redefine mostrar_info() para incluir su carrera.
    # ---------------------------------------------
    def mostrar_info(self):
        return (f"Estudiante: {self._nombre} {self._apellido} ({self._genero}), "
                f"{self._edad} años - Carrera: {self.carrera}")


class Docente(Persona):
    def __init__(self, nombre, apellido, genero, edad, especialidad):
        super().__init__(nombre, apellido, genero, edad)
        self.especialidad = especialidad

    # Polimorfismo nuevamente aplicado
    def mostrar_info(self):
        return (f"Docente: {self._nombre} {self._apellido} ({self._genero}), "
                f"{self._edad} años - Especialidad: {self.especialidad}")


# ============================================
#     PROGRAMA PRINCIPAL (uso de las clases)
# ============================================

p1 = Persona("Luis", "González", "M", 30)
e1 = Estudiante("María", "Pérez", "F", 20, "Ingeniería")
d1 = Docente("Ana", "Ramírez", "F", 40, "Programación")

print(p1.mostrar_info())
print(e1.mostrar_info())  # ejemplo de polimorfismo
print(d1.mostrar_info())  # ejemplo de polimorfismo

# Usando encapsulación (modificando datos de forma controlada)
p1.set_nombre("Luis Alberto")
p1.set_edad(31)
print(p1.mostrar_info())
