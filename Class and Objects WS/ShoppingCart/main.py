from customer import Customer
from product import Product


customer1 = Customer("Wes")
print(customer1.name)
product1 = Product("Cream Chesse", 3, "Dairy")
product2 = Product("Bagel Bites", 7, "Bread")
product3 = Product("Grill", 150, "Appliances")
customer1.place_item_in_cart(product1)
customer1.place_item_in_cart(product2)
customer1.place_item_in_cart(product3)
customer1.review_items_in_cart()
customer1.take_all_items_out()
customer1.review_items_in_cart()