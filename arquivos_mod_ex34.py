import os

#Declarando variáveis globais
valor:int=0
dir:str=""
arq:str=""

def mult(vlr,tab):

    res:int=tab*vlr

    return res #Variável de retorno
#Fim-mult

def grava(c,rslt):
    global dir,arq

    #Var locais
    file:str=''
    tipo:str=''
    enc:str=''
    linha:str=''

    linha = str(rslt) + '\n' #Convertendo resultado pra string 

    #Verificando se o diretório existe e se é um diretório
    if(os.path.exists(dir) and os.path.isdir(dir)):

        enc = "utf-8"

        #Verificando se o arquivo existe e se o contador é maior que 0
        if(os.path.exists(dir +"/"+ arq) and os.path.isfile(dir +"/"+ arq) and c>0):
            tipo = 'a'
        else:
            tipo ='w'         
        #Fim-condição 2

        with open(dir+"/"+arq,tipo, encoding=enc) as file:
            file.write(linha)
        #Gravando a linha no arquivo
    #Fim-condição 1
#Fim-grava

def main():
    global dir, valor, arq 

    dir = '/tmp/exercicios' #Caminho da pasta

    os.makedirs(dir, exist_ok=True) #Criando a pasta e verificando se já existe
    os.chmod(dir,0o744) #Dando permissão

    arq = 'ex34.txt' #Recebendo exercício

    #Var locais
    cont:int=0
    result:int=0

    valor = int(input('Digite um valor para calcular sua tabuada: '))

    #Loop
    for cont in range(0,11):
        result = mult(valor,cont)
        grava(cont,result)
    #Fim-loop
#Fim-main

if (__name__ == '__main__'):
    main()
#Chamando o main