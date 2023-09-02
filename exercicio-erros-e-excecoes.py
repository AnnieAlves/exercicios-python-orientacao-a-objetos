# O programa abaixo deve calcular a média dos valores digitados pelo usuário.
# No entanto, ele não está funcionando bem. Você pode consertá-lo?


#
# def calcular_media(valores):
#     tamanho = 1
#     soma = 0.0
#     for i, valor in enumerate(valores):
#         soma += valor
#         i += 1
#     media = soma / tamanho
#
# continuar = True
# valores = []
# while continuar:
#     valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
#     if valor.lower() == 'ok':
#         continuar = false
#
# media = calcular_media(valores)
# print('A média calculada para os valores {} foi de {}'.format(valores, media))


# Programa corrigido:


def calcular_media(valores):
    tamanho = 0  # o Tamanho deve começar em 0 para funcionar no laço for
    soma = 0.0
    for valor in valores:
        soma += valor
        tamanho += 1

    if tamanho == 0:  # Caso o tamanho seja 0, ou seja, o usuário não tenha digitado, evita divisão por zero
        media = soma / 1
    else:
        media = soma / tamanho

    return media  # A função não retornava nenhum valor, agora ela retorna o que queremos


continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')

    if valor.lower() == 'ok':
        continuar = False  # Corrigido o erro de syntax: Era "false" e mudei para "False"
    else:  # Caso o valor digitado não seja "ok", ele segue
        try:  # Tenta converter para float, para assegurar que o usuário não tenha errado a digitação
            valor = float(valor)  # Converte para float
            valores.append(valor)  # O código anterior não adicionava os valores à lista, mas agora usa o append

        except ValueError:
            print("Valor inválido. Digite apenas números")

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))
