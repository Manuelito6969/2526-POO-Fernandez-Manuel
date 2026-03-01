import unittest
from PARCIAL_2.SEMANA_11.producto import Producto if False else None
# The above import is a fallback in case of package layout; we'll import dynamically in tests
import importlib
import sys
import os

# Ajustar path para importar desde la carpeta del proyecto
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root not in sys.path:
    sys.path.insert(0, root)

producto_mod = importlib.import_module('PARCIAL 2.SEMANA 11.producto'.replace(' ', ' ')) if False else None
# Simpler dynamic import: find the file directly
try:
    from PARCIAL_2.SEMANA_11.producto import Producto
except Exception:
    # Try direct relative import path (Windows folder names contain spaces; fallback to file import)
    import importlib.util
    spec = importlib.util.spec_from_file_location('producto', os.path.join(root, 'PARCIAL 2', 'SEMANA 11', 'producto.py'))
    producto = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(producto)
    Producto = producto.Producto

class TestProducto(unittest.TestCase):
    def test_creacion_valida(self):
        p = Producto(1, 'Manzana', 10, 0.5)
        self.assertEqual(p.id, 1)
        self.assertEqual(p.nombre, 'Manzana')
        self.assertEqual(p.cantidad, 10)
        self.assertAlmostEqual(p.precio, 0.5)

    def test_invalidos(self):
        with self.assertRaises(ValueError):
            Producto('x', 'Nombre', 1, 1.0)
        with self.assertRaises(ValueError):
            Producto(2, '', 1, 1.0)
        with self.assertRaises(ValueError):
            Producto(3, 'A', -1, 1.0)
        with self.assertRaises(ValueError):
            Producto(4, 'A', 1, -5.0)

    def test_to_from_dict(self):
        p = Producto(5, 'Pera', 3, 0.75)
        d = p.to_dict()
        self.assertEqual(d['nombre'], 'Pera')
        self.assertEqual(d['cantidad'], 3)
        self.assertAlmostEqual(d['precio'], 0.75)
        p2 = Producto.from_dict(5, d)
        self.assertEqual(p2.id, 5)
        self.assertEqual(p2.nombre, 'Pera')

if __name__ == '__main__':
    unittest.main()

