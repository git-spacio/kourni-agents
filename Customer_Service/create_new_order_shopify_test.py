import sys
sys.path.append('/home/snparada/Spacionatural/Libraries')
from shopify_lib.orders import ShopifyOrders
import time

def main():
    # Inicializar la clase
    shopify = ShopifyOrders()
    
    # Email del cliente
    customer_email = "snparada@spacionatural.cl" 
    
    # Lista de productos a agregar
    products = [
        {
            'variant_id': 43547586756777,  # Cera Candelilla
            'quantity': 1
        },
        {
            'variant_id': 44546989392041,  # Aceite de Almendras 30 ml
            'quantity': 1
        }
    ]
    
    try:
        # Crear nuevo draft order
        draft_id, payment_url = shopify.create_new_draft_order(products, customer_email)
        
        if draft_id and payment_url:
            print(f"\nDraft order created successfully!")
            print(f"Draft order ID: {draft_id}")
            print(f"\nPayment URL:")
            print(payment_url)
        else:
            print("\nError creating draft order")
                
    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    main()