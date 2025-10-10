print("___TEMPERATURA AMBIENTAL___")
#lista con los datos base
datos=[
    ("MONTERREY",29),
    ("CDMX", 26),
    ("TLAXCALA", 30),
    ("PUEBLA", 28),
    ("MAZATLAN", 33)
]
 #listas de comprehrension
temp_min = 30
temperaturas_filtradas= [registro for registro in datos
if registro[1] >=temp_min ]
print(f"\nDatos filtrados: {temperaturas_filtradas}")

def obtener_temperatura(registro):
    return registro[1]

registros_ordenados = sorted(datos, key=obtener_temperatura,
                             reverse=True
                             )
print(f"\nREGISTROS ORDENADOS (DECENDENTE):{registros_ordenados}")
 #sim map y lambda
alertas_calor= [f"alerta de calor en {ciudad} {temp}ªC"
                 for ciudad, temp in registros_ordenados]
print(f"\nALTAS TEMPERATURAS")
print(*alertas_calor, sep="\n")

solo_temperaturas =[temp for ciudad, temp in registros_ordenados]
 #suma de las temperaturas
suma_temp=sum(solo_temperaturas)
 #promedio
promedio=suma_temp / len(solo_temperaturas)
print(f"\npromedio es: {promedio:.4}ªC ")