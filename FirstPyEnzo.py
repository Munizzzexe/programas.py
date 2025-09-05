#apresentação
print ('Meu nome é Enzo, tenho 13 anos e estudo programação em python.')

#nome
print('Qual é o seu nome?')
nome = input()

#validaçao do nome
if nome == (""):
    while True: 
        nome == ("")
        print ('Porfavor, digite seu nome') 
        nome = input()
        if nome != (""):
              break

print ('Muito prazer', nome )

#idade
print('Qual é a sua idade?')
idade = input ()

#validaçao da idade
if idade == (""):
    while True:
        idade == ("")
        print ('Porfavor, digite sua idade')

        idade = input()
        if idade != (""):
   
              break 
        
if not idade.isdigit():
    while True:
            idade.isdigit() == False
            print ('Por favor, digite uma idade valida')
            idade = input()
            if idade.isdigit() == True:
                  break

idade = int(idade)

if idade < 0 or idade > 120:
    while True:
            idade < 0 or idade > 120
            print ('Por favor, digite uma idade verdadeira você não pode ter essa idade')
            idade = input()
            idade = int(idade)
            if not (idade < 0 or idade > 120):
                  break

#informaçoes
print ('Nossa, você tem', idade, 'anos!')
print ('Que legal', nome, ' você gosta de programar?')
gosta = input ()