num=int(input("Digite el numero que quiera covertir: "))
bas=int(input("Digite la base que quiera convertir: "))
def convertir_Entero_Base(numero, base):
    conversion_cadena="0123456789ABCDEF"
    if numero < base:
        resultado = conversion_cadena[numero]
    else:
        resultado=convertir_Entero_Base(numero//base, base)+conversion_cadena[numero % base]
    return resultado

ejecutar=convertir_Entero_Base(num,bas)
print(f"El numero {num} a base {bas} es: {ejecutar}")
