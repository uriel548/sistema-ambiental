import pandas as pd
df1=pd.read_csv("C:/Users/ALVA/Documents/respuesta correctassss.csv",header=0)
df1.drop(index=1)
df2=pd.read_csv("C:/Users/ALVA/Documents/respuestas del cuentionario - Respuestas de formulario 1.csv",header =0)

print(df1)
print(df2)

