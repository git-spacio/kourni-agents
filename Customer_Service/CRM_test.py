import sys
sys.path.append('/home/snparada/Spacionatural/Libraries')

from odoo_lib.crm import OdooCRM
from odoo_lib.customers import OdooCustomers
import pandas as pd

def buscar_cliente(customers_df, rut=None, email=None, id=None):
    """Busca un cliente por RUT, email o ID"""
    if id:
        cliente = customers_df[customers_df['id'] == id]
    elif rut:
        cliente = customers_df[customers_df['vat'] == rut]
    elif email:
        cliente = customers_df[customers_df['email'] == email]
    else:
        return None
    
    return None if cliente.empty else cliente.iloc[0]

def crear_oportunidad(crm, cliente_id, nombre_oportunidad="Nueva Oportunidad"):
    """Crea una oportunidad y verifica su creación"""
    # Convertir numpy.int64 a int de Python
    cliente_id = int(cliente_id)
    
    # Crear diccionario base con campos requeridos
    opportunity_data = {
        'name': nombre_oportunidad,
        'partner_id': cliente_id,
        'expected_revenue': 1000.0,
        'probability': 50.0,
        'type': 'opportunity'  # Asegurarnos que sea una oportunidad
    }
    
    # Eliminar cualquier campo que sea None
    opportunity_data = {k: v for k, v in opportunity_data.items() if v is not None}
    
    opportunity_id = crm.create_oportunity(opportunity_data)
    if isinstance(opportunity_id, str):
        print(f"Error al crear oportunidad: {opportunity_id}")
        return None
    
    # Verificar que se creó correctamente
    oportunidad = crm.read_oportunity_by_id(opportunity_id)
    if not isinstance(oportunidad, pd.DataFrame):
        print(f"Error al verificar oportunidad: {oportunidad}")
        return None
    
    return opportunity_id

def crear_cotizacion(crm, opportunity_id, productos):
    """Crea una cotización para una oportunidad"""
    quotation_id = crm.create_quotation_from_opportunity(opportunity_id, productos)
    if isinstance(quotation_id, str):
        print(f"Error al crear cotización: {quotation_id}")
        return None
    return quotation_id

# Inicializar conexiones
crm = OdooCRM(database='test')
customers = OdooCustomers(database='test')
customers_df = customers.read_all_customers_in_df()

# Buscar cliente (puedes usar cualquiera de estos métodos)
cliente = buscar_cliente(customers_df, id=4860)
# cliente = buscar_cliente(customers_df, email="pazibarra.j@gmail.com")
# cliente = buscar_cliente(customers_df, rut="11275171-8")

if cliente is None:
    print("Cliente no encontrado")
else:
    print(f"Cliente encontrado: {cliente['name']}")
    
    # Crear oportunidad
    opportunity_id = crear_oportunidad(crm, cliente['id'])
    
    if opportunity_id:
        print(f"Oportunidad creada con ID: {opportunity_id}")
        
        # Definir productos para la cotización
        productos = [
            {
                'product_id': 3059,
                'product_uom_qty': 2.0
            },
            {
                'product_id': 3564,
                'product_uom_qty': 1.0
            }
        ]
        
        # Crear cotización
        quotation_id = crear_cotizacion(crm, opportunity_id, productos)
        
        if quotation_id:
            print(f"Cotización creada con ID: {quotation_id}")
