class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def total_cart_value(self):
        total = sum(p.price * p.quantity for p in self.cart_items)
        print(f"Valoarea totală a coșului: {total}")
        return total

    def show_cart(self):
        for product in self.cart_items:
            product.display_info()
