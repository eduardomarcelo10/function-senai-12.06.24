# Função que calcula o imc \tem como parametros de entrada (peso, altura).
def imc (peso, altura):
    calculo = peso / (altura * altura)
    return calculo

# Função que retorna a "categoria" que tem como argumento o IMC.
def categoria_imc (imc):

    abaixo = "1-ABAIXO DO PESO!"
    normal = "2 - NORMAL!"
    acima = "3 - ACIMA DO PESO!"
    ob1 = "4 - OBESIDADE GRAU 1!"
    ob2 = "5 - OBESIDADE GRAU 2!"

    if (imc <= 18.5 ):
        return abaixo

    if (imc >= 18.6 ) and (imc <= 24.9):
        return normal

    if (imc >= 25 ) and (imc <= 29.9):
        return acima

    if (imc >= 30) and (imc <= 39.9):
        return ob1

    if (imc > 40):
        return ob2


# Função principal do nosso programa
if __name__ == '__main__':
    continuar = 's'

    while (continuar == 's'):
        p = float(input("Digite o peso: "))
        a = float(input("Digite a altura: "))
        imc_calculado = imc (p, a)
        print ("Seu IMC é: ", imc_calculado)

        # Imprimir categoria do IMC
        categoria = categoria_imc (imc_calculado)
        print (categoria)
        continuar = input ("Desejo calcular novamente? (s/n):")
