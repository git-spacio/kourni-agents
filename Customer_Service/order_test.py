import sys
sys.path.append('/home/snparada/Spacionatural/Libraries')
from shopify_lib.orders import ShopifyOrders
import pandas as pd
from pprint import pprint

shopify_orders = ShopifyOrders()
order = shopify_orders.read_order_by_number('63983')

pprint(order)

shipping_info = order['shipping_lines'][0]
courier = shipping_info['title']  # 'STARKEN - Domicilio'
shipping_method = shipping_info['source']  # 'Envíos Personalizados'
shipping_cost = shipping_info['price']  # '6886'

customer_info = order['customer']
customer_name = customer_info['name'] # Muy importante para guardar su contacto en whatsapp y hablar con la persona por su nombre
customer_name = customer_info['last_name'] # Muy importante para guardar su contacto en whatsapp
customer_email = customer_info['email']
customer_phone = customer_info['phone']
