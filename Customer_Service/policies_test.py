import sys
sys.path.append('/home/snparada/Spacionatural/Libraries')
from shopify_lib.policies import ShopifyPolicies

# Inicializar
policies = ShopifyPolicies()

# Obtener todas las políticas
refund_policy = policies.read_refund_policy()
privacy_policy = policies.read_privacy_policy()
terms_policy = policies.read_terms_of_service()
shipping_policy = policies.read_shipping_policy()

# Imprimir cada política
print("\n=== POLÍTICA DE REEMBOLSO ===")
print(f"Título: {refund_policy['title']}")
print(f"Contenido: {refund_policy['body']}")

print("\n=== POLÍTICA DE PRIVACIDAD ===")
print(f"Título: {privacy_policy['title']}")
print(f"Contenido: {privacy_policy['body']}")

print("\n=== TÉRMINOS DE SERVICIO ===")
print(f"Título: {terms_policy['title']}")
print(f"Contenido: {terms_policy['body']}")

print("\n=== POLÍTICA DE ENVÍO ===")
print(f"Título: {shipping_policy['title']}")
print(f"Contenido: {shipping_policy['body']}")
