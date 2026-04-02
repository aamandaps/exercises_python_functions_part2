import os

#Declarando as variáveis globais
nome:str=''
nota1:float=0.0
nota2:float=0.0
nota3:float=0.0
nota4:float=0.0
valor_media:float=0.0
dir:str=''
arq:str=''

def entrada():
    global nota1,nota2,nota3,nota4,valor_media,nome

    #Recebendo os valores
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))

    valor_media = med(nota1,nota2,nota3,nota4) #Chamando o cálculo da média

    print(f'A média é igual a: {valor_media:.2f}') #Média no console

    cadastro(nome,nota1,nota2,nota3,nota4,valor_media)
#Fim-entrada

def med(n1,n2,n3,n4):
    media:float=0.0

    media = (n1+n2+n3+n4)/4
    return media
#Fim-med  

def cadastro(nm,nt1,nt2,nt3,nt4,vlr_media):
    global dir,arq
    
    linha:str=''
    linha = nm+';'+str(nt1)+';'+str(nt2)+';'+str(nt3)+';'+str(nt4)+';'+str(vlr_media) + '\n' #Convertendo resultado pra string e concatenando

    escreveArq(dir,arq,linha)
#Fim-cadastro

def escreveArq(caminho,arquivo,linha_arq):
    file:str=''
    tipo:str=''
    enc:str=''
 
    enc = 'utf-8'

    #Verificando se o diretório existe e se é um diretório
    if (os.path.exists(caminho) and os.path.isdir(caminho)):

        #Verificando se o arquivo existe e se é um arquivo
        if(os.path.exists(caminho+"/"+arquivo) and os.path.isfile(caminho+"/"+arquivo)):
            tipo='a'
        else:
            tipo='w'
        #Fim-condição 2

        with open(caminho+"/"+arquivo,tipo,encoding=enc) as file:
            file.write(linha_arq)
        #Gravando no arquivo
    #Fim-condição 1
#Fim-escreveArq


def main():
    global dir, arq 

    dir = '/tmp/exercicios' #Caminho da pasta

    os.makedirs(dir, exist_ok=True) #Criando a pasta e verificando se já existe
    os.chmod(dir,0o744) #Dando permissão

    arq = 'ex21.txt' #Recebendo exercício

    #Iniciando loop de entrada
    cont:int=0
    while cont<5:

        entrada() #Chamando o input
        cont += 1
    #Fim-loop
#Fim-main

if (__name__ == '__main__'):
    main()
#Chamando o main