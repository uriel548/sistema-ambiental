from functools import reduce, wraps
from typing import Callable
import time

#decoradores
def medir_tiempo(fun:Callable):
    def wrapper(*args, **kwargs):
        inicio:float= time.time()
        fun(*args, **kwargs)
        fin: float = time.time()
        print(f"TIEMPO DE EJECUCUION {fin - inicio:.4f} segundos")
    return wrapper

def auditar_funcion(func):
    if not hasattr(func,"__llamadas_contador"):
        func.__llamadas_contador = 0
    def wrapper(*args, **kwargs):
        func.__llamadas_contador += 1

        nombre_funcion=func.__name__
        conteo= func.__llamadas_contador
        print(f"ejecutando funcion: `{nombre_funcion}`")
        print(f"LLAMADA NUMERO: {conteo}")

        resultado= func(*args, **kwargs)
        return resultado
    return wraps(func)(wrapper)


#GRNERADOR DE DATOS
def leer_temperatura():
    datos=[
        ("MONTERREY",29),
        ("CDMX", 26),
        ("TLAXCALA", 30),
        ("PUEBLA", 28),
        ("MAZATLAN", 33)
    ]

    for registro in datos:
        yield registro

#1filtrer y lambda (reutilizables)

def filtro_temperatura(registros,temp_min=30):
    return list(filter(lambda registro: registro[1] >= temp_min, registros))
#3ORDENAR DE FORMA DESCENDENTE

@auditar_funcion
def ordenar_temp(registros):
    return sorted(registros, key=lambda registro:registro[1], reverse=True)

#2transformacion com map
def alertas(registros_ordenados):
    return list(map(lambda registro: f"ALERTA DE CALOR EN [{registro[0]}]: [{registro[1]}]ºC", registros_ordenados))

#4calcular el promedio mediante reduce
def promedio(registros):
    if not registros:
        return 0.0, 0
    suma_temp= reduce(lambda x,y: x + y[1], registros, 0)
    total_registros= len(registros)
    promedio= suma_temp / total_registros

    return promedio, suma_temp

#funcion principal
def main():
    print("---SISTEMA DE TEMPERATURA AMBIENTAL---")
#0
    base_original=list(leer_temperatura())
    print(f"\nBASE DE DATOS:{base_original}")
#1
    filtrado_temp= filtro_temperatura(base_original)
    print(f"\nREGISTROS FILTRADOS (MAYORES O IGUALES A 30:{filtrado_temp}")
#2
    registros_ordenados=ordenar_temp(base_original)
    print(f"\nREGISTROS ORDENADOS (DESCENDENTE): {registros_ordenados}")
#3
    alertas_finales= alertas(base_original)
    print(f"\nALERTAS DE CALOR: {alertas_finales}")
#4
    promedio_general, suma_temp= promedio(registros_ordenados)
    print(f"\nTEMPERATURA PROMEDIO DE ALERTAS: {promedio_general:.1f}ºC")





if __name__=="__main__":
    main()
