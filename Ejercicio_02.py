#Definimos una funcion para obtener caracter equivalentes
def caracter_hexadecimal(valor):
    valor = str(valor)
    equivalencias = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",}
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor
#Definimos una funcion convertir
def decimal_hexadecimal(decimal):
    hexadecimal = " "
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


decimal = int(input("Digite un número decimal que quiere convertir en hexadecimal: "))
hexadecimal = decimal_hexadecimal(decimal)
print(f"El decimal {decimal} en hexadecimal es: {hexadecimal}")
