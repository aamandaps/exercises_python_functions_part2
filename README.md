## Baseado no Ex. 34, fazer:
a. Criar no Linux a pasta /tmp/exercicios <br>
<p>i. Assegurar que ela tem permissão 744 (Fazer em Python)</p>
<br>b. Declarar como globais, as variáveis:
<p>i. valor: int = 0 </p>
<p>ii. dir: str = ‘’</p>
<p>iii. arq: str = ‘’</p>
<p>iv. arq: str = ‘’</p><br>
c. Um procedimento main() que use valor como global e inicie uma variável contador
e uma variável result, locais, peça ao usuário um valor entre 1 e 10 e chame 10 vezes
a função mult(vlr, tab), passando o valor e o contador como parâmetros. O retorno
da função deve ser retornado para a variável result. Por fim, ainda dentro da
estrutura de repetição, deve-se chamar o procedimento grava(c, rslt), passando o
contador e o result como parâmetros;<br>
d. A função mult deve receber o valor passado pelo usuário e o contador, deve
declarar uma variável local res, que recebe a multiplicação de vlr e tab e é a variável
de retorno da função;<br>
e. O procedimento grava recebe como parâmetros o contador da estrutura de
repetição e o resultado da multiplicação. Utilizando dir e arq como globais, que
devem ter dir = ‘/tmp/exercicios’ e arq = ‘ex34.txt’, deve declarar file, tipo, enc e linha
como str vazios. A variável linha deve receber o cast da variável rslt (str(rslt))
concatenado com uma quebra de linha (‘\n’). Criar, baseado no material de aula,
deve-se verificar se o diretório existe e é diretório e, em sendo verdadeiro, verificar
se o arquivo existe (Para definir se o tipo da operação será w (write) ou a (append)),
mas só pode mudar o tipo para ‘a’, se c for maior que 0. Gravar a linha no arquivo.<br>
## 2. Baseado no Ex. 21, fazer:
a. Criar no Linux a pasta /tmp/exercicios
<p>i. Assegurar que ela tem permissão 744 (Fazer em Python)</p><br>
b. Declarar como globais, as variáveis:
<p>i. nome: str = ‘’</p>
<p>ii. nota1, nota2, nota3, nota4, valor_media  float</p>
<p>iii. dir: str = ‘’</p>
<p>iv. arq: str = ‘’</p><br>
c. Um procedimento main() que inicie uma variável contador, local e chame 5 vezes o
procedimento entrada;<br>
d. O procedimento entrada, usando os globais nome, nota1, nota2, nota3, nota4 e
valor_media, pede a entrada do nome, das notas, chama uma função med(n1, n2,
n3, n4) que calcula e retorna o valor da média aritmética, exiba em console a média
e, por fim, chame o procedimento cadastro(nm, nt1, nt2, nt3, nt4, vlr_med);<br>
e. A função med, recebe como parâmetros, as 4 notas, inicializa uma variável local
media (float), que recebe o cálculo da média aritmética das notas e será o retorno
da função;<br>
f. O procedimento cadastro, recebe o nome do aluno, as 4 notas e a média como
parâmetros, declara linha, como str e usa arq e dir como globais que devem ter dir
= ‘/tmp/exercicios’ e arq = ‘ex21.txt’ . A variável linha deve receber uma operação de
concatenar de nome, todas as notas e a média, sempre separados por ‘;’ e com
quebra de linha ‘\n’ ao final. As variáveis numéricas, para serem concatenadas,
devem passar por uma operação de cast (str(n1)). Por fim, deve chamar o
procedimento escreveArq(caminho, arquivo, linha_arq).<br>
g. A função escreveArq recebe, como parâmetros, o nome do diretório, o nome do
arquivo e a linha concatenada, para ser gravada no arquivo. Deve declarar file, tipo
e enc como str vazios. Baseado no material de aula, deve-se verificar se o diretório
existe e é diretório e, em sendo verdadeiro, verificar se o arquivo existe (Para definir
se o tipo da operação será w (write) ou a (append)) e gravar no arquivo o conteúdo
da variável linha_cad.
