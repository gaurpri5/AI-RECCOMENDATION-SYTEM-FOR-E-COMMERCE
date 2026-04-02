import reflex as rx


class State(rx.State):

    # User Login
    user = ""

    # Cart
    cart = []

    # Wishlist
    wishlist = []

    # Orders
    orders = []

    # Browsed Products
    browsed = []

    # Recommended Products
    recommendations = []

    # Add to Cart
    def add_to_cart(self, item):
        self.cart.append(item)

    # Add to Wishlist
    def add_to_wishlist(self, item):
        self.wishlist.append(item)

    # Add Browsed Product
    def add_browsed(self, item):
        self.browsed.append(item)

    # Place Order
    def place_order(self):
        self.orders = self.orders + self.cart
        self.cart = []