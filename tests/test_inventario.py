import unittest
import os
import tempfile
import importlib.util
import sys

# Ajustar path raíz
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root not in sys.path:
    sys.path.insert(0, root)

# Cargar inventario desde archivo
spec = importlib.util.spec_from_file_location('inventario', os.path.join(root, 'PARCIAL 2', 'SEMANA 11', 'inventario.py'))
mod_inv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod_inv)
Inventario = mod_inv.Inventario

specp = importlib.util.spec_from_file_location('producto', os.path.join(root, 'PARCIAL 2', 'SEMANA 11', 'producto.py'))
mod_prod = importlib.util.module_from_spec(specp)
specp.loader.exec_module(mod_prod)
Producto = mod_prod.Producto

class TestInventario(unittest.TestCase):
    def setUp(self):
        # Crear archivo temporal para inventario
        fd, path = tempfile.mkstemp(prefix='test_inv_', suffix='.json')
        os.close(fd)
        self.tmpfile = path
        # Asegurarnos de que el archivo empiece vacío
        with open(self.tmpfile, 'w', encoding='utf-8') as f:
            f.write('{}')
        self.inv = Inventario(archivo=self.tmpfile)

    def tearDown(self):
        try:
            os.remove(self.tmpfile)
        except Exception:
            pass

    def test_agregar_eliminar_actualizar(self):
        p = Producto(10, 'Naranja', 5, 1.2)
        self.inv.agregar_producto(p)
        # Verificar que esté en inventario
        resultados = self.inv.buscar_por_nombre('Naranja')
        self.assertEqual(len(resultados), 1)
        # Actualizar
        self.inv.actualizar_producto(10, nueva_cantidad=8, nuevo_precio=1.5)
        p2 = self.inv.productos[10]
        self.assertEqual(p2.cantidad, 8)
        self.assertAlmostEqual(p2.precio, 1.5)
        # Eliminar
        self.inv.eliminar_producto(10)
        self.assertNotIn(10, self.inv.productos)

    def test_persistencia_roundtrip(self):
        p = Producto(20, 'Melon', 2, 3.0)
        self.inv.agregar_producto(p)
        # Crear nueva instancia cargando desde el mismo archivo
        inv2 = Inventario(archivo=self.tmpfile)
        self.assertIn(20, inv2.productos)
        self.assertEqual(inv2.productos[20].nombre, 'Melon')

    def test_agregar_duplicado(self):
        p = Producto(30, 'Uva', 1, 0.5)
        self.inv.agregar_producto(p)
        with self.assertRaises(ValueError):
            self.inv.agregar_producto(Producto(30, 'Uva duplicada', 2, 0.6))

    def test_eliminar_no_existente(self):
        with self.assertRaises(KeyError):
            self.inv.eliminar_producto(9999)

if __name__ == '__main__':
    unittest.main()

