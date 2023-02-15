

resposta = ""


#definindo as funcoes
def somar(primeiro_numero,segundo_numero):
    return primeiro_numero + segundo_numero

def subtrair(primeiro_numero,segundo_numero):
    return primeiro_numero - segundo_numero
    
def multiplicar(primeiro_numero,segundo_numero):
    return primeiro_numero * segundo_numero

def dividir(primeiro_numero,segundo_numero):
    return primeiro_numero / segundo_numero

def potencia(primeiro_numero,segundo_numero):
    return primeiro_numero ** segundo_numero

def raiz(primeiro_numero,segundo_numero):
    return primeiro_numero ** (1 / segundo_numero)

#bloco principal
while resposta != "S":

    print("-----------------CALCULADORA PYTHON-----------------\n") 
    print("SELECIONE A OPERACAO QUE DESEJA REALIZAR:")
    print("\n 1- ADICIONAR\n 2- SUBTRAIR\n 3- DIVIDIR\n 4- MULTIPLICAR\n 5 - POTENCIACAO\n 6 - RADICIACAO")
    operacao = input("\nDIGITE 1,2,3,4,5 OU 6: ")
    primeiro_numero = float(input("\nDIGITE O PRIMEIRO NUMERO: "))
    segundo_numero = float(input("\nDIGITE O SEGUNDO NUMERO: "))

#identificando operacao a realizar & imprimindo resultados
    if operacao == "1":
        print("\nO RESULTADO DA SOMA E: ", somar(primeiro_numero,segundo_numero))
    elif operacao == "2":
        print("\nO RESULTADO DA SUBTRACAO E: ", subtrair(primeiro_numero,segundo_numero))
    elif operacao == "3" and segundo_numero != 0:
        print("\nO RESULTADO DA DIVISAO E: ", dividir(primeiro_numero,segundo_numero))
    elif operacao == "4":
        print("\nO RESULTADO DA MULTIPLICACAO E: ", multiplicar(primeiro_numero,segundo_numero))
    elif operacao == "5":
        print("\nO RESULTADO DA POTENCIACAO E: ", potencia(primeiro_numero,segundo_numero))
    elif operacao == "6" and segundo_numero != 0:
        print("\nO RESULTADO DA RAIZ E:", raiz(primeiro_numero,segundo_numero))
    else:
        print("\nOPERACAO INVALIDA! ")

#testando se o usuario continuara na aplicacao ou finalizara
    resposta = input("\nDIGITE S PARA SAIR OU QUALQUER TECLA PARA REALIZAR UMA NOVA OPERACAO: ").upper()
    
    




    


   


