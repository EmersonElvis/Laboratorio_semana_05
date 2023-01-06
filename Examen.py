#Funcion
def potencia_recursiva(base,exponente):
    """ Precondición: exponente debe ser mayor o igual que cero.
        Devuelve: base\^exponente. """

    # Caso base
    if exponente <= 0:
        resultado_f=1
    else:
        # exponente par
        if exponente % 2 == 0:
            resultado_i = potencia_recursiva(base, exponente/2)
            resultado_f=resultado_i*resultado_i
        # exponente impar
        else:
            resultado_i = potencia_recursiva(base, (exponente-1)/2)
            resultado_f= resultado_i * resultado_i * base
    return resultado_f
    
print(potencia_recursiva(2,8))
