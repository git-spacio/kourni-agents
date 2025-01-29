import sys
sys.path.append('/home/snparada/Spacionatural/Libraries')
from enviame_lib.shipping import EnviameAPI
import pandas as pd
from dotenv import load_dotenv
import os

def buscar_envio_shopify(referencia):
    
    enviame = EnviameAPI()
    
    # Buscar el envío
    envio = enviame.read_delivery_by_reference(referencia)
    
    if envio is not None:
        print("\n=== Detalles del Envío ===\n")
        print(f"ID Enviame: {envio['ID']}")
        print(f"Nº Referencia: {envio['Nº Referencia']}")
        print(f"Tracking: {envio['Tracking']}")
        print(f"Estado: {envio['Estado']}")
        print(f"Info Estado: {envio['Info Estado']}")
        print(f"Fecha Estado: {envio['Fecha Estado']}")
        print(f"Transportista: {envio['Transportista']}")
        print(f"Cliente: {envio['Cliente']}")
        print(f"Dirección: {envio['Dirección']}")
        print(f"Ciudad: {envio['Ciudad']}")
        print(f"PDF Etiqueta: {envio['PDF Etiqueta']}")
        return envio
    return None

def buscar_tracking_enviame(referencia):
    enviame = EnviameAPI()
    
    # Buscar el tracking
    tracking = enviame.read_tracking_by_reference(referencia)
    
    if tracking is not None and 'data' in tracking:
        print("\n=== Historial de Tracking ===\n")
        for evento in tracking['data']['tracking']:
            print(f"Fecha: {evento['created_at']}")
            print(f"Estado: {evento['name']}")
            print(f"Descripción: {evento['comment']}")
            print("------------------------")
        return tracking['data']
    return None

if __name__ == "__main__":
    # envio = buscar_envio_shopify("64221")
    tracking = buscar_tracking_enviame("64221")