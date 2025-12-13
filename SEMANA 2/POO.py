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

from typing import Optional


class Persona:
    def __init__(self, nombre: str, apellido: str, genero: str, edad: int):
        # =====================================================
        # 2. ENCAPSULAMIENTO (Protección de los datos)
        # -----------------------------------------------------
        # Los atributos están protegidos usando un guion bajo,
        # lo que indica que no deben ser modificados directamente.
        #
        # Además, se utilizan propiedades (getters/setters) para
        # controlar el acceso a estos datos. Esto permite:
        # - Validar valores antes de asignarlos
        # - Proteger la integridad de la información
        # - Evitar cambios directos no controlados
        #
        # =====================================================
        self._nombre: Optional[str] = None
        self._apellido: Optional[str] = None
        self._genero: Optional[str] = None
        self._edad: Optional[int] = None

        # Usar los setters para validar desde el inicio
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.edad = edad

    # -------- METODO DE ABSTRACCIÓN --------
    def mostrar_info(self) -> str:
        return f"{self._nombre} {self._apellido} ({self._genero}), {self._edad} años"

    # -------- PROPIEDADES (encapsulamiento) --------
    @property
    def nombre(self) -> Optional[str]:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre.strip()) > 1:
            self._nombre = nuevo_nombre.strip()

    @property
    def apellido(self) -> Optional[str]:
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido: str) -> None:
        if isinstance(nuevo_apellido, str) and len(nuevo_apellido.strip()) > 1:
            self._apellido = nuevo_apellido.strip()

    @property
    def genero(self) -> Optional[str]:
        return self._genero

    @genero.setter
    def genero(self, nuevo_genero: str) -> None:
        if isinstance(nuevo_genero, str) and nuevo_genero.strip():
            self._genero = nuevo_genero.strip()

    @property
    def edad(self) -> Optional[int]:
        return self._edad

    @edad.setter
    def edad(self, nueva_edad: int) -> None:
        if isinstance(nueva_edad, int) and nueva_edad > 0:
            self._edad = nueva_edad

    # Mantener compatibilidad con get_/set_ (opcional)
    def get_nombre(self) -> Optional[str]:
        return self.nombre

    def set_nombre(self, nuevo_nombre: str) -> None:
        self.nombre = nuevo_nombre

    def get_edad(self) -> Optional[int]:
        return self.edad

    def set_edad(self, nueva_edad: int) -> None:
        self.edad = nueva_edad


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
    def __init__(self, nombre: str, apellido: str, genero: str, edad: int, carrera: str):
        # Llama al constructor de Persona
        super().__init__(nombre, apellido, genero, edad)
        self._carrera: Optional[str] = None
        self.carrera = carrera

    # ---------------------------------------------
    # 4. POLIMORFISMO: metodo mostrar_info() redefinido
    # ---------------------------------------------
    # El polimorfismo permite que el mismo metodo (mostrar_info)
    # funcione diferente según el tipo de objeto.
    #
    # Aquí, Estudiante redefine mostrar_info() para incluir su carrera.
    # ---------------------------------------------
    @property
    def carrera(self) -> Optional[str]:
        return self._carrera

    @carrera.setter
    def carrera(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._carrera = valor.strip()

    def mostrar_info(self) -> str:
        return (f"Estudiante: {self._nombre} {self._apellido} ({self._genero}), "
                f"{self._edad} años - Carrera: {self.carrera}")


class Docente(Persona):
    def __init__(self, nombre: str, apellido: str, genero: str, edad: int, especialidad: str):
        super().__init__(nombre, apellido, genero, edad)
        self._especialidad: Optional[str] = None
        self.especialidad = especialidad

    @property
    def especialidad(self) -> Optional[str]:
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._especialidad = valor.strip()

    # Polimorfismo nuevamente aplicado
    def mostrar_info(self) -> str:
        return (f"Docente: {self._nombre} {self._apellido} ({self._genero}), "
                f"{self._edad} años - Especialidad: {self.especialidad}")


# ============================================
#     PROGRAMA PRINCIPAL (uso de las clases)
# ============================================

if __name__ == "__main__":
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
