from product import Product


class ShoppingCart:
    def __init__(self):
        self.what_is_in_the_cart = []
        self.total_of_items_in_cart = 0
        self.number_of_items_in_cart = 0
        
    def add_item_to_cart(self, name, price, category):
        item = Product(name, price, category)
        self.what_is_in_the_cart.append(item)
        print(f'{item.name} successfully added to cart! ')

    def remove_all_items_from_cart(self):
        self.what_is_in_the_cart = [] 
        
    def get_total_of_cart(self):
        total = 0
        for item in self.what_is_in_the_cart:
            add_this = item.price
            total += add_this
        print(f'Total of cart is ${total} \n')