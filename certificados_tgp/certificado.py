import openpyxl
import pandas as pd

# Leer el archivo ENTE.xlsx usando openpyxl
df_ente = pd.read_excel('D:\mefi\certificados_tgp\ENTE.xlsx', sheet_name='ENTE', engine='openpyxl')
print(df_ente.head())