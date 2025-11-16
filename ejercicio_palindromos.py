#ejericio 4 fraces de palindromos
#ceramos la funcion
#se compara letra por letra despues de invertir el texto eliminando los espacios
def verificar_palabra(texto):
    preparar_texto = "".join(c for c in texto if c.isalpha()).lower()
    return len(preparar_texto) >1 and preparar_texto ==preparar_texto[::-1]

#utilizamos while true para que solo las letras sean aceptadas sin numeros y signos
def main():
    while True:
        palabra= input("ingresa un texto: ")
#comprobamos que no se ingresen numeros
        validacion_palabra = palabra.replace (' ', '')
        if validacion_palabra.isalpha():
            break
        else:
            print("ERROR: INGRESA SOLO TEXTO NO NUMEROS(intenta de nuevo). ")

#verificamos el texto o palabra ingresado
    if verificar_palabra(palabra):
     print(f"'{palabra}' es un palindromo")
    else:
     print(f"'{palabra}' no es un palindromo")

if __name__ == "__main__":
    main()


