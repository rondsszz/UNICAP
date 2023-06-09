#Calculadora (Rondon Guilherme)
def somar(a, b):
    return a + b
    
def subtrair(a, b):
    return a - b
    
def multiplicar(a, b):
    x = 0
    for _ in range(b):
        x = somar(x, a)
    return x
    
def dividir_quo(a, b):
    quociente = 0
    while a >= b:
        a = subtrair(a, b)
        quociente = somar(quociente, 1)
    return quociente
    
def dividir_resto(a, b):
    while a >= b:
        a = subtrair(a, b)
    return a
    
def elevar(a, b):
    y = 1
    for _ in range(b):
        y = multiplicar(y, a)
    return y
    
def calcular(a, operador, b):
    if operador == '+':
        return somar(a, b)
    elif operador == '-':
        return subtrair(a, b)
    elif operador == '*':
        return multiplicar(a, b)
    elif operador == '/':
        return dividir_quo(a, b)
    elif operador == '%':
        return dividir_resto(a, b)
    elif operador == '^':
        return elevar(a, b)
        
def main():
    a, operador, b = input().split()
    a = int(a)
    b = int(b)
    resultado = calcular(a, operador, b)
    print(resultado)
main()
