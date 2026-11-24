#Store Information
store_name = "Mira's Event Supplies"
store_address = "123 Event Street, City, State"
customer_name = "Sarah Johnson"
product_name = "LED Fairy Lights"

#Product Information
unit_price = 8500.0
item_purchased = 2
total_stock =  20
delivery_fee = 2500.0

#Payment Status
payment_confirmed = True

#Arithimetic Operations
subtotal = unit_price * item_purchased

grand_total = subtotal + delivery_fee

average_cost_per_item = grand_total / item_purchased

remaining_stock = total_stock - item_purchased


#Display customer receipt

print("========= Customer Receipt =========")
print(f"Store Name: {store_name}")
print('====================================')

print(f"Customer Name: {customer_name}")
print(f"Product Name: {product_name}")
print(f"Unit Price: ₦{unit_price:.2f}")
print(f"Quantity Purchased: {item_purchased}")

print("------------------------------------")
print(f"Subtotal: ₦{subtotal:.2f}")
print(f"Delivery Fee: ₦{delivery_fee:.2f}")
print(f"Grand Total: ₦{grand_total:.2f}")
print(f"Average Cost per Item: ₦{average_cost_per_item:.2f}")

print("------------------------------------")
print(f"Remaining Stock: {remaining_stock} items")

print("payment status:", "confirmed" if payment_confirmed else "pending")

print("====================================")
print("Thank you for shopping with us!")
print("====================================")
