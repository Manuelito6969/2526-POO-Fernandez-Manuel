"""
PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
Programa para calcular el promedio semanal de temperaturas
Autor: Estudiante UEA - TICs
Asignatura: Programación Orientada a Objetos
Mejoras realizadas: manejo de argumentos, validación de entradas, tipos y modo no interactivo para pruebas.
"""

from __future__ import annotations
from typing import List, Optional, Tuple
import argparse
import sys


class Clima:
    """
    Clase que representa la información climática diaria.

    Contiene el día y la temperatura registrada.
    """

    def __init__(self, dia: str, temperatura: float = 0.0) -> None:
        """Constructor de la clase Clima.

        Args:
            dia (str): Nombre del día de la semana
            temperatura (float): Temperatura en grados Celsius (default: 0.0)
        """
        self.__dia = dia
        self.__temperatura = float(temperatura)

    # Métodos getter y setter (encapsulamiento)
    def get_dia(self) -> str:
        """Retorna el día de la semana."""
        return self.__dia

    def get_temperatura(self) -> float:
        """Retorna la temperatura registrada."""
        return self.__temperatura

    def set_temperatura(self, temperatura: float) -> None:
        """Establece la temperatura del día.

        Args:
            temperatura (float): Temperatura en grados Celsius
        """
        self.__temperatura = float(temperatura)

    def mostrar_info(self) -> None:
        """Muestra la información del clima del día."""
        print(f"  {self.__dia:12} : {self.__temperatura:6.2f} °C")

    def __repr__(self) -> str:
        return f"Clima(dia={self.__dia!r}, temperatura={self.__temperatura!r})"


class SemanaClimatica:
    """
    Clase que representa una semana completa de datos climáticos.
    Gestiona el conjunto de datos de temperatura de los 7 días.
    """

    DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def __init__(self) -> None:
        """Constructor que inicializa la semana con los 7 días."""
        self.__dias_clima: List[Clima] = [Clima(dia) for dia in self.DIAS_SEMANA]

    def ingresar_temperaturas(self, temperaturas: Optional[List[float]] = None, interactive: bool = True) -> None:
        """
        Método para ingresar las temperaturas de todos los días de la semana.
        Si se provee `temperaturas`, las usa (debe tener 7 valores). Si no, entra en modo interactivo.
        """
        if temperaturas is not None:
            if len(temperaturas) != len(self.__dias_clima):
                raise ValueError(f"Se requieren {len(self.__dias_clima)} temperaturas, pero se recibieron {len(temperaturas)}.")
            for clima, temp in zip(self.__dias_clima, temperaturas):
                self._validar_y_asignar(clima, temp)
            return

        # Modo interactivo
        print("=" * 50)
        print("INGRESO DE TEMPERATURAS DIARIAS")
        print("=" * 50)

        for clima in self.__dias_clima:
            while True:
                try:
                    raw = input(f"Ingrese la temperatura del {clima.get_dia()} (°C): ").strip()
                    # Permitir comas decimales y espacios
                    raw = raw.replace(',', '.')
                    temp = float(raw)
                    self._validar_y_asignar(clima, temp)
                    break
                except ValueError:
                    print("Error: Por favor ingrese un valor numérico válido (ej: 23.5).")

    def _validar_y_asignar(self, clima: Clima, temp: float) -> None:
        """Valida rango razonable de temperatura y asigna al objeto Clima."""
        if not (-100.0 <= temp <= 100.0):
            raise ValueError(f"Temperatura {temp} fuera de rango razonable (-100 a 100 °C).")
        clima.set_temperatura(temp)

    def calcular_promedio(self) -> float:
        """Calcula el promedio de temperaturas de la semana."""
        suma = sum(clima.get_temperatura() for clima in self.__dias_clima)
        promedio = suma / len(self.__dias_clima)
        return promedio

    def obtener_temperatura_maxima(self) -> Tuple[float, str]:
        """Encuentra la temperatura máxima de la semana."""
        temp_max = max(self.__dias_clima, key=lambda c: c.get_temperatura())
        return temp_max.get_temperatura(), temp_max.get_dia()

    def obtener_temperatura_minima(self) -> Tuple[float, str]:
        """Encuentra la temperatura mínima de la semana."""
        temp_min = min(self.__dias_clima, key=lambda c: c.get_temperatura())
        return temp_min.get_temperatura(), temp_min.get_dia()

    def mostrar_resultados(self) -> None:
        """Muestra todos los resultados del análisis semanal de temperaturas."""
        print("\n" + "=" * 50)
        print("RESULTADOS DEL ANÁLISIS SEMANAL")
        print("=" * 50)

        print("\nTemperaturas registradas:")
        for clima in self.__dias_clima:
            clima.mostrar_info()

        promedio = self.calcular_promedio()
        temp_max, dia_max = self.obtener_temperatura_maxima()
        temp_min, dia_min = self.obtener_temperatura_minima()

        print("\n" + "-" * 50)
        print(f"Promedio semanal: {promedio:.2f} °C")
        print(f"Temperatura máxima: {temp_max:.2f} °C ({dia_max})")
        print(f"Temperatura mínima: {temp_min:.2f} °C ({dia_min})")
        print("=" * 50)


class SistemaClimatico:
    """
    Clase principal que gestiona la interfaz del sistema.
    Actúa como controlador de la aplicación.
    """

    def __init__(self) -> None:
        self.__semana: Optional[SemanaClimatica] = None

    def mostrar_menu(self) -> None:
        """Muestra el menú principal del sistema."""
        print("\n" + "=" * 50)
        print("SISTEMA DE ANÁLISIS DE TEMPERATURA SEMANAL")
        print("Programación Orientada a Objetos")
        print("=" * 50)
        print("1. Ingresar temperaturas y calcular promedio")
        print("2. Salir")
        print("=" * 50)

    def ejecutar_interactivo(self) -> None:
        """Ejecución en modo interactivo con menú."""
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.__semana = SemanaClimatica()
                try:
                    self.__semana.ingresar_temperaturas()
                    self.__semana.mostrar_resultados()
                except ValueError as e:
                    print(f"Error al ingresar temperaturas: {e}")

            elif opcion == "2":
                print("\n¡Gracias por usar el sistema!")
                print("Programa finalizado.")
                break

            else:
                print("\nOpción no válida. Por favor seleccione 1 o 2.")

    def ejecutar_no_interactivo(self, temperaturas: List[float]) -> None:
        """Ejecución en modo no interactivo: recibe una lista de 7 temperaturas y muestra resultados."""
        self.__semana = SemanaClimatica()
        try:
            self.__semana.ingresar_temperaturas(temperaturas=temperaturas, interactive=False)
            self.__semana.mostrar_resultados()
        except ValueError as e:
            print(f"Error: {e}")


def parse_temps_arg(arg: str) -> List[float]:
    """Parsea una cadena con temperaturas separadas por comas a una lista de floats."""
    parts = [p.strip().replace(',', '.') for p in arg.split(',') if p.strip()]
    if not parts:
        raise ValueError("La lista de temperaturas está vacía.")
    try:
        temps = [float(p) for p in parts]
    except ValueError:
        raise ValueError("Todas las temperaturas deben ser valores numéricos.")
    return temps


def main(argv: Optional[List[str]] = None) -> int:
    """Función principal que expone opciones no interactivas para pruebas.

    Opciones:
    --auto : ejecuta con un conjunto de ejemplo predefinido
    --temps "t1,t2,...,t7" : lista de 7 temperaturas separadas por comas
    Si no se pasan opciones, se entra en modo interactivo.
    """
    parser = argparse.ArgumentParser(description="Sistema de análisis de temperatura semanal")
    parser.add_argument('--auto', action='store_true', help='Usar conjunto de ejemplo automático (no interactivo).')
    parser.add_argument('--temps', type=str, help='Lista de 7 temperaturas separadas por comas. Ej: --temps "23,24,22,20,19,18,21"')
    args = parser.parse_args(argv)

    sistema = SistemaClimatico()

    if args.auto:
        ejemplo = [20.0, 21.5, 19.0, 22.0, 18.7, 17.3, 20.5]
        print("Modo automático: uso de datos de ejemplo.")
        sistema.ejecutar_no_interactivo(ejemplo)
        return 0

    if args.temps:
        try:
            temps = parse_temps_arg(args.temps)
        except ValueError as e:
            print(f"Error al parsear --temps: {e}")
            return 2
        if len(temps) != 7:
            print(f"Error: se requieren exactamente 7 temperaturas; se recibieron {len(temps)}.")
            return 3
        sistema.ejecutar_no_interactivo(temps)
        return 0

    # Modo interactivo por defecto
    try:
        sistema.ejecutar_interactivo()
    except KeyboardInterrupt:
        print('\nInterrumpido por el usuario. Saliendo...')
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
