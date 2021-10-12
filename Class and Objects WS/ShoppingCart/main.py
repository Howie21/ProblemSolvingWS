from customer import Customer


customer1 = Customer("Wes")
print(customer1.name)
customer1.place_item_in_cart("Cream Chesse", 3, "Dairy")
customer1.place_item_in_cart("Bagel Bites", 7, "Bread")
customer1.place_item_in_cart("Grill", 150, "Appliances")
customer1.review_items_in_cart()
customer1.take_all_items_out()
customer1.review_items_in_cart()