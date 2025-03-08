import sys
sys.path.append('/home/snparada/Spacionatural/Libraries')
from mercado_pago_lib.payments import MercadoPagoPayment

# Inicializar el cliente de Mercado Pago
mp_payment = MercadoPagoPayment()

def generate_payment_link(product_name, price, quantity=1, description=None, payer_email=None):
    """
    Genera un link de pago para un producto.
    
    Args:
        product_name (str): Nombre del producto
        price (float): Precio del producto
        quantity (int): Cantidad de productos
        description (str): Descripción del producto
        payer_email (str): Email del pagador
    
    Returns:
        str: URL del link de pago o mensaje de error
    """
    # Crear los datos de la preferencia
    preference_data = {
        "items": [
            {
                "title": product_name,
                "quantity": quantity,
                "unit_price": price,
                "description": description or product_name,
            }
        ],
        "back_urls": {
            "success": "https://www.tu-sitio.com/success",
            "failure": "https://www.tu-sitio.com/failure",
            "pending": "https://www.tu-sitio.com/pending"
        },
        "auto_return": "approved",
    }
    
    # Agregar información del pagador si se proporciona
    if payer_email:
        preference_data["payer"] = {
            "email": payer_email
        }
    
    # Crear la preferencia
    preference = mp_payment.create_preference(preference_data)
    
    # Verificar si la creación fue exitosa
    if isinstance(preference, dict) and "init_point" in preference:
        return {
            "payment_link": preference["init_point"],
            "preference_id": preference["id"]
        }
    else:
        return f"Error al generar link de pago: {preference}"

# Ejemplo de uso
payment_info = generate_payment_link(
    product_name="Producto Ejemplo",
    price=100.00,
    description="Descripción detallada del producto",
    payer_email="cliente@ejemplo.com"
)
print(payment_info)
