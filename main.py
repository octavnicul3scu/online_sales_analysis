from product import Product
from product_manager import ProductManager

manager = ProductManager()

# Adaugare produse
manager.add_product(Product("Produs A", 10, 5))
manager.add_product(Product("Produs B", 15, 3))
manager.add_product(Product("Produs C", 20, 2))

# Afisare produse si valoare totala
manager.show_products()
manager.total_value()
