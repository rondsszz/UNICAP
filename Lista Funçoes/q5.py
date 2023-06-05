#Questão 5 lista para praticar
def valorPagamento(valor, dias_atraso):
    multa = valor * 0.03
    juros = valor * (dias_atraso * 0.001)
    total = valor + multa + juros
    return total

prestacoes_pagas = 0
valor_total_pagamento = 0

while True:
    valor_prestacao = float(input("Informe o valor da prestação (ou 0 para sair): "))
    
    if valor_prestacao == 0:
        break
    
    dias_atraso = int(input("Informe o número de dias em atraso: "))
    
    valor_a_pagar = valorPagamento(valor_prestacao, dias_atraso)
    prestacoes_pagas += 1
    valor_total_pagamento += valor_a_pagar
    
    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}\n")

print(f"Relatório do dia:")
print(f"Quantidade de prestações pagas: {prestacoes_pagas}")
print(f"Valor total recebido: R$ {valor_total_pagamento:.2f}")
