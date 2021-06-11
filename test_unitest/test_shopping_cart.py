import unittest
from shopping_cart import Item, ShoppingCart, NotExistItemError

class TestShoppingCart(unittest.TestCase):

    def setUp(self) -> None:
        self.pan = Item("Pan", 7.0)
        self.jugo = Item("Jugo", 9.0)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)


    def tearDown(self) -> None:
        pass


    def test_cinco_mas_cinco_igual_diez(self):
        assert 5 + 5 == 10

# assertEqual
    def test_nombre_priducto_igual_manzana(self):
        self.assertEqual(self.pan.name, "Pan")

# assertNotEqual
    def test_nombre_producto_diferente_manzana(self):
        self.assertNotEqual(self.jugo.name, "Manzana")

# assertTrue
    def test_contiene_productos(self):
        self.assertTrue(self.shopping_cart.contains())

# assertFalse
    def test_no_contiene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains())

#Testear excepciones
    def test_exception_obtain_juice(self):
        with self.assertRaises(NotExistItemError):
            self.shopping_cart.get_item(self.jugo)


if __name__ == "__main__":
    unittest.main()