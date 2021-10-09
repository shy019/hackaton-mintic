import sqlite3
import datetime
import pandas as pd
import numpy as np
from pandas._libs.tslibs import period               


con = sqlite3.connect('db.sqlite3')


sql = '''
SELECT * FROM clientes_parqueadero ;
'''

df = pd.read_sql_query(sql,con)
print(df.columns)
df.groupby(['hora_puesto','placa_vehiculo_id']).count()
print(df.groupby)

print(df['hora_puesto'].value_counts())

print(len(df)) #Y también podemos usar la función len para que nos diga cuántos registros tiene este dataframe:

df.info()
df['hora_puesto']= pd.to_timedelta(df['hora_puesto'], errors='coerce')



print("Valor regulario de cada parqueadero: {}".format(df['hora_puesto'].mean()))
print("Hora mas frecuente de parqueo : {}".format(df['hora_puesto'].mode()))



"""
dt_init = pd.timedelta_range('00:00:00', periods=24 ,  freq ='H')
print(dt_init)

dt_init = pd.timedelta_range(start='00:00:00', end='23:59:00', freq='H' )
print(dt_init)
s = pd.Series(np.arange(24), index=dt_init)
print(s)

print(s.resample('1H').mean())
"""
#df.set_index("gastos_totales",inplace=True)


df['hora_puesto']= pd.to_numeric(df['hora_puesto'], errors='coerce')

