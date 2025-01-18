import sys
sys.path.append('/home/snparada/Spacionatural/Libraries')
from sheets_lib.main_sheets import GoogleSheets

# Los posible courier son Starken, BLue Express y Recibelo
# IMPROTANTE, el precio Agencia y a Domicilio son los mismos en Starken
sheet_starken = GoogleSheets('1I21ydjtqny9Xy22YHuHHrB888KHtpXbj9_YU53VdeEY')
starken_matrix = sheet_starken.read_dataframe('Starken Shopify')

print(starken_matrix)

sheet_bluexpress = GoogleSheets('1LXoMG3BhZFRbuSEdO82Pe9RV0kI0VRSGQEFUqrg1Dck')
bluexpress_matrix = sheet_bluexpress.read_dataframe('Blue Shopify')

print(bluexpress_matrix)

sheet_recibelo = GoogleSheets('1A3kbmkJK0Ujmg3jaLjVFzUHqsjEhn8F_7SrMi7uFSJM')
recibelo_matrix = sheet_recibelo.read_dataframe('Recibelo Shopify')

print(recibelo_matrix)
