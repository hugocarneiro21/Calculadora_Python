def bem_vindo():

    print("************************************")
    print("**********Calculadora***************")
    print("************************************")

bem_vindo()

def calculadora():
    operacao = input ('''Digite a operação:
                  + para Soma;
                  - para Subtração;
                  * para Multiplicação;
                  / para Divisão \n''')

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número numero: "))

    if operacao == '+':
        print (f'{numero1} + {numero2} = {numero1 + numero2}')
    elif operacao == '-':
         print (f'{numero1} - {numero2} = {numero1 - numero2}')
    elif operacao == '*':
         print (f'{numero1} * {numero2} = {numero1 * numero2}')
    elif operacao == '/':
         print (f'{numero1} / {numero2} = {numero1 / numero2}')
    else:
         print(' Você precisa digitar a operação correta')
    finalizar()


def finalizar():
   #verificaremos se a pessoa deseja continuar calculando
    calculadora_continuar = input('Você deseja continuar calculando? Digite "S" para sim e "N" para não: \n')
    print(f'Você digitou: {calculadora_continuar}')
    
    if(calculadora_continuar.upper() =='S'):
        print('Continuando a calcular...')
        calculadora()

    elif(calculadora_continuar.upper() =='N'):
        print('Tudo bem, nos vemos depois...')
    
    else:
        finalizar()
calculadora()
