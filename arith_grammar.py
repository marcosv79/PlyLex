import ply.yacc as yacc
from arith_lexer import ArithLexer

class ArithGrammar:
    tokens = ArithLexer.tokens

    precedence = (
        ('left', 'MAIS', 'MENOS'),
        ('left', 'MULT', 'DIVISAO'),
        ('right', 'simetrico'),
    )

    symbols = {}

    def __init__(self):
        self.parser = None
        self.lexer = ArithLexer()
        self.tokens = self.lexer.tokens
        self.ast = None

    def build(self, **kwargs):
        self.lexer.build(**kwargs)
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, string):
        return self.parser.parse(string, lexer=self.lexer.lexer)

    def p_decl(self, p):
        """ D   : A
                | E
        """
        p[0] = p[1]
        self.ast = p[0]

    def p_expr_increment(self, p):
            """ E : E INCREMENT"""
            p[0] = {
                "op": "INCREMENT",
                "args": [p[1]]
            }
            self.ast = p[0]  # Atualizar o atributo ast

    def p_expr_maisigual(self,p):
            """ E : E MAIS_IGUAL E PONTO_VIRGULA"""
            p[1] += p[3]
            p[0] = p[1]
            self.ast = p[0]  # Atualizar o atributo ast

    def p_expr_escrever(self, p):
        """
        E : ESCREVER STRING PONTO_VIRGULA
          | ESCREVER E PONTO_VIRGULA
          | ESCREVER E VIRGULA E PONTO_VIRGULA
          | ESCREVER STRING VIRGULA E PONTO_VIRGULA
          | ESCREVER E VIRGULA STRING PONTO_VIRGULA
        """
        if len(p) == 4:
            p[0] = {
                "op": "ESCREVER",
                "args": [p[2]]
            }
        elif len(p) == 6:
            args = [p[2], p[4]]
            p[0] = {
                "op": "ESCREVER",
                "args": args
            }
        else:
            p[0] = None

    def p_expr_soma(self, p):
        """ E : E MAIS E """
        p[0] = {
            "op": "MAIS",
            "args": [p[1], p[3]]
        }
        self.ast = p[0]  # Atualizar o atributo ast

    def p_expr_mult(self, p):      
        """ E : E MULT E """
        p[0] = {
            "op": "MULT",
            "args": [p[1], p[3]]
        }
        self.ast = p[0]  # Atualizar o atributo ast
    
    def p_expr_sub(self, p):      
        """ E : E MENOS E """
        p[0] = {
            "op": "MENOS",
            "args": [p[1], p[3]]
        }
        self.ast = p[0]  # Atualizar o atributo ast
        
    def p_expr_sinalmenos(self, p): 
        " E : MENOS E %prec simetrico "
        p[0] = -p[2]
        
    def p_expr_pare(self, p):      
        """ E : LPAR E RPAR """
        p[0]= p[2]
    
    def p_expr_num(self, p):      
        """ E : NUMERO  """
        p[0]= p[1]
        
    def p_expr_var(self, p):      
        """ E : ID  """
        if p[1] in ArithGrammar.symbols:
            p[0]= ArithGrammar.symbols[ p[1] ] 
        else:
            raise Exception(f"error: '{p[1]}' undeclared (first use in this function)")

    def p_expr_div(self, p):
        """ E : E DIVISAO E """
        # Verificar se o divisor é zero
        if p[3] == 0:
            print("Erro: divisão por zero")
            p[0] = 0
        else:
            p[0] = {
                "op": "DIVISAO",
                "args": [p[1], p[3]]
            }
            self.ast = p[0]  # Atualizar o atributo ast

    def p_expr_comentario(self, p):
        """
        E : COMENTARIO_UMA_LINHA
          | COMENTARIO_MULTIPLAS_LINHAS
        """
        pass

    def p_atrib(self, p):
        """ A : ID IGUAL E PONTO_VIRGULA """
        self.symbols[p[1]] = p[3]
        p[0] = self.symbols[p[1]]

    def p_decl_var(self, p):
        """D : VAR var_list PONTO_VIRGULA """
        p[0] = {'op': 'VAR', 'args': p[2]}

    def p_var_list(self, p):
        """var_list : var_item
                    | var_item VIRGULA var_list"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]

    def p_var_item(self, p):
        """var_item : ID IGUAL constant """
        self.symbols[p[1]] = p[3]
        p[0] = (p[1], p[3])

    def p_constant(self, p):
        """constant : NUMERO
                    | STRING"""
        p[0] = p[1]

    def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.value}'")
        else:
            print("Syntax error at EOF")