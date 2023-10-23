[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/lID0UNno)
# Processamento de Linguagens (ESI)
## TP02 

### grupo  D09     

| Número  |                 Nome                 |
| ------- | ------------------------------------ |
| 18568   | Marcos Alberto Lopes de Vasconcelos  |
| 20457   | Tomás Fernandes Ferreira             |
| 20468   | Diogo Miguel Barbosa de Oliveira     |

### Estrutura do Projeto
  [/doc](./doc)   relatório do trabalho prático
  
## Objetivos
Este trabalho prático tem como objetivo desenvolver uma ferramenta em Python utilizando a biblioteca PLY que seja capaz de interpretar uma linguagem de entrada e especificar algumas instruções que habitualmente se observam em linguagens de programação.
Inicialmente a ferramenta deverá começar por ler um ficheiro de entrada (entrada.ea) contendo uma sequência de instruções de especificação de expressões aritméticas.

## Linguagem para expressoes aritméticas
 A linguagem especifica expressões aritméticas por meio de instruções de escrita, declaração, atribuição e saída, permitindo que valores sejam exibidos, variáveis sejam declaradas e atribuídas, e interações com o utilizador sejam realizadas. As instruções são as seguintes:
- Instrução de escrita;
- Declaração de variáveis;
- Atribuição a uma variável;
- Ciclos;
- Funções;
- Comentários e outras instruções.

## Descrição dos ficheiros
#### arith_main.py
Ficheiro principal onde são construídos os lexer e parser, é lido o ficheiro de entrada, é avaliado o programa e convertido na linguagem C e finalmente é apresentado o resultado.

#### arith_lexer.py
Ficheiro do analisador léxico.

#### arith_grammar.py
Ficheiro do analisador sintático.

#### arith_lexer_test.py
Ficheiro para testar o analisador léxico.

#### arith_grammar_test.py
Ficheiro para testar o analisador sintático.

#### arith_eval.py
Ficheiro para avaliação da AST.

#### arith_c.py
Ficheiro para converter as instruções em linguagem C.

#### output.c
Ficheiro onde é apresentado o conteúdo traduzido em linguaguem C.

#### entrada.ea
Ficheiro de entrada que recebe as instruções a serem realizadas.

#### gramatica.txt
Ficheiro onde é especificada a gramática da linguagem de entrada.