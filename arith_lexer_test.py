from arith_lexer import ArithLexer

al = ArithLexer()
al.build()
al.input("VAR f=10; ESCREVER [(f+1)]; //comentario") 

while True:
    tk = al.token() 
    if not tk: 
        break
    print(tk,end="\n")