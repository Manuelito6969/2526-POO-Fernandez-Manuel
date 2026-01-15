# Tarea: Implementar un sistema de gestión de biblioteca utilizando POO
# Tema: Sistema de Gestión de Biblioteca

# 1. DEFINICIÓN DE CLASE BASE
class Libro:
    """Clase base que representa un libro en la biblioteca"""

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo  # Atributo público
        self.autor = autor  # Atributo público
        self.isbn = isbn  # Atributo público

    def mostrar_info(self):
        """Metodo que será sobrescrito (Polimorfismo)"""
        print(f" Libro: '{self.titulo}' por {self.autor}")
        print(f"   ISBN: {self.isbn}")


# 2. DEFINICIÓN DE CLASE DERIVADA (Herencia)
class LibroDigital(Libro):
    """Clase derivada que representa un libro digital"""

    def __init__(self, titulo, autor, isbn, formato, tamaño_mb):
        # Uso de super() para heredar atributos de la clase base
        super().__init__(titulo, autor, isbn)
        self.formato = formato  # PDF, EPUB, MOBI, etc.

        # 3. ENCAPSULACIÓN
        # Atributo privado para proteger el tamaño del archivo
        self.__tamaño_mb = tamaño_mb

    # Metodo Getter para acceder al atributo encapsulado
    def obtener_tamaño(self):
        """Retorna el tamaño del archivo en MB"""
        return self.__tamaño_mb

    # Metodo Setter con validación
    def actualizar_tamaño(self, nuevo_tamaño):
        """Actualiza el tamaño del archivo con validación"""
        if nuevo_tamaño > 0 and nuevo_tamaño < 500:
            self.__tamaño_mb = nuevo_tamaño
            print(f"✅ Tamaño actualizado a {self.__tamaño_mb} MB")
        else:
            print("❌ Error: El tamaño debe estar entre 0 y 500 MB")

    # 4. POLIMORFISMO (Sobrescritura de metodo)
    def mostrar_info(self):
        """Sobrescribe el metodo de la clase base Libro"""
        print(f"💻 Libro Digital: '{self.titulo}' por {self.autor}")
        print(f"   ISBN: {self.isbn}")
        print(f"   Formato: {self.formato} | Tamaño: {self.__tamaño_mb} MB")

    def descargar(self):
        """Metodo exclusivo de LibroDigital"""
        print(f"⬇️  Descargando '{self.titulo}' ({self.__tamaño_mb} MB)...")
        print(f"   Formato: {self.formato}")


# 3. SEGUNDA CLASE DERIVADA (Herencia múltiple de conceptos)
class LibroFisico(Libro):
    """Clase derivada que representa un libro físico"""

    def __init__(self, titulo, autor, isbn, paginas, ubicacion):
        super().__init__(titulo, autor, isbn)
        self.paginas = paginas

        # ENCAPSULACIÓN: Atributo privado para la ubicación en estantería
        self.__ubicacion = ubicacion
        self.__prestado = False  # Estado del libro

    def obtener_ubicacion(self):
        """Getter para la ubicación"""
        return self.__ubicacion

    def prestar_libro(self):
        """Metodo para prestar el libro"""
        if not self.__prestado:
            self.__prestado = True
            print(f"✅ Libro '{self.titulo}' prestado exitosamente")
        else:
            print(f"❌ El libro '{self.titulo}' ya está prestado")

    def devolver_libro(self):
        """Metodo para devolver el libro"""
        if self.__prestado:
            self.__prestado = False
            print(f"✅ Libro '{self.titulo}' devuelto exitosamente")
        else:
            print(f"⚠️  El libro '{self.titulo}' no estaba prestado")

    # POLIMORFISMO: Sobrescribe mostrar_info
    def mostrar_info(self):
        """Versión específica para libros físicos"""
        estado = "Prestado" if self.__prestado else "Disponible"
        print(f"📖 Libro Físico: '{self.titulo}' por {self.autor}")
        print(f"   ISBN: {self.isbn} | Páginas: {self.paginas}")
        print(f"   Ubicación: {self.__ubicacion} | Estado: {estado}")


# --- DEMOSTRACIÓN DE FUNCIONALIDAD ---
if __name__ == "__main__":
    print("=" * 60)
    print("🏛️  SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("=" * 60)

    # Creación de objetos (Instancias)
    libro_base = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0307474728")
    libro_digital = LibroDigital("El Principito", "Antoine de Saint-Exupéry",
                                 "978-0156012195", "PDF", 2.5)
    libro_fisico = LibroFisico("Don Quijote de la Mancha", "Miguel de Cervantes",
                               "978-8424936471", 863, "Estante A-3")

    print("\n--- 🔄 DEMOSTRACIÓN DE POLIMORFISMO ---")
    print("El mismo método 'mostrar_info()' se comporta diferente:\n")

    libro_base.mostrar_info()
    print()
    libro_digital.mostrar_info()
    print()
    libro_fisico.mostrar_info()

    print("\n--- 🔒 DEMOSTRACIÓN DE ENCAPSULACIÓN ---")
    print("Los atributos privados solo se acceden con métodos:\n")

    # Acceso controlado al tamaño del archivo
    print(f"Tamaño actual: {libro_digital.obtener_tamaño()} MB")
    libro_digital.actualizar_tamaño(3.2)  # Válido
    libro_digital.actualizar_tamaño(600)  # Inválido

    print()

    # Sistema de préstamos con encapsulación
    print(f"Ubicación del libro físico: {libro_fisico.obtener_ubicacion()}")
    libro_fisico.prestar_libro()
    libro_fisico.prestar_libro()  # Intento de prestar dos veces
    libro_fisico.devolver_libro()

    print("\n--- 📥 FUNCIONALIDAD ADICIONAL ---")
    libro_digital.descargar()

    print("\n" + "=" * 60)
    print("✅ Demostración completada exitosamente")
    print("=" * 60)