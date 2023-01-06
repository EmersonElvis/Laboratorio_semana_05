n=int(input("Digite un número n: "))
p=int(input("Digite un número p: "))

def suma_recursiva(a,b):
    if a==0 and b!=0:
        suma=suma*(b+suma_recursiva(a,b-1))
    elif b==0 and a!= 0:
        suma=a
    elif a==0 and b==0:
        suma = 0
    else:
        suma = a+b*(suma_recursiva(a,b-1))
        if b==1:
            return suma-a
    return suma

print(suma_recursiva(n,p))
