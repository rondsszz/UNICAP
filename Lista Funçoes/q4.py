def converter(horas, minutos):
    if horas == 0:
        h2 = 12
        periodo = 'A.M'
    elif horas < 12:
        h2 = horas
        periodo = 'A.M'
    elif horas == 12:
        h2 = 12
        periodo = 'P.M'
    else:
        h2 = horas - 12
        periodo = 'P.M'
    return h2, minutos, periodo

def exibir(horas, minutos, periodo):
    print(f'{horas}:{minutos:02d} {periodo}')

def main():
    horas = int(input())
    minutos = int(input())
    h2, minutos, periodo = converter(horas, minutos)
    exibir(h2, minutos, periodo)
main()
