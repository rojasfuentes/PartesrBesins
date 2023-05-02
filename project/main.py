#from loadFile import orden_path, inventario_path
import pandas as pd

orden_path = r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\Parser\Besins\Besisns\CICLO 4.1.xlsx'
inventario_path = r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\Parser\Besins\Besisns\Consulta de Inventario (1).xlsx'
nota = '104'

idf = '0423'

#Orden
df = pd.read_excel(orden_path, header= 3)
df = df.iloc[:, [0, 1, 2, 5 , 6, 7, 8]]
df_inventario = pd.read_excel(inventario_path, header= 4)
df_inventario = df_inventario.iloc[:, [1, 5, 9, 13]]


previous_id = ''
value = 0

def add_nota(row):
    global previous_id
    global value
    global nota
    value += 1
    current_id = row['Bill TO']
    if current_id != previous_id:
        value = 0
        previous_id = current_id
    
    return value + 1


df['Id.Pedido Cliente'] = df['Id. Pedido'] + idf
df['Linea'] = df.apply(add_nota, axis=1)

for i in range(len(df)):
    if '-' in str(df.loc[i, 'Lote']):
        df.loc[i, 'CODIGO'] = df.loc[i, 'Lote']
    else:
        df.loc[i, 'CODIGO'] = df.loc[i, 'CODIGO']
print(df.tail(15))
#print(df_inventario.keys())
