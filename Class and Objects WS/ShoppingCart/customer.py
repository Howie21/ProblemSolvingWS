from shopping_cart import ShoppingCart 


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()
    
    def place_item_in_cart(self, item):
        self.cart.add_item_to_cart(item)
    
    def take_all_items_out(self):
        self.cart.remove_all_items_from_cart()
        print(f'All items removed! ')

    def get_total_of_items(self):
        self.cart.get_total_of_cart()

    def review_items_in_cart(self):
        
        if self.cart.what_is_in_the_cart == []:
            print('There is nothing in the cart\n')
        elif self.cart.what_is_in_the_cart != []:
            print(f'All items in the cart are as follows \n')
            for item in self.cart.what_is_in_the_cart:
                print(f"{item.name} ")
            self.cart.get_total_of_cart()
    
    