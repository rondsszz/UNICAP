#Questão 3 lista para praticar
def somaImposto(taxaImposto, custo):
    imposto= custo*taxaImposto
    valorfinal= custo+imposto
    return valorfinal
def main():
    taxaImposto= float(input())
    custo= float(input())
    print(f'R$ {somaImposto(taxaImposto, custo):.2f}')
main()

