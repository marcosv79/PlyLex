import ply.lex as lex

class ArithLexer:
    reservadas = {
        'ESCREVER' : 'ESCREVER',
        'VAR': 'VAR',
        'PARA': 'PARA',
        'EM': 'EM',
        'FAZER': 'FAZER',
        'FIMPARA': 'FIMPARA'
}

    tokens = [
        'ID',
        'NUMERO',
        'MAIS',
        'MENOS',
        'MULT',
        'DIVISAO',
        'IGUAL',
        'INCREMENT',
        'MAIS_IGUAL',
        'VIRGULA',
        'PONTO_VIRGULA',
        'LPAR',
        'RPAR',
        'LBRACKET',
        'RBRACKET',
        'STRING',
        'COMENTARIO_UMA_LINHA',
        'COMENTARIO_MULTIPLAS_LINHAS',
        'ALEATORIO',
    ] + list(reservadas.values())

    t_MAIS = r'\+'
    t_MENOS = r'-'
    t_MULT = r'\*'
    t_DIVISAO = r'/'
    t_IGUAL = r'='
    t_INCREMENT = r'\+\+'
    t_MAIS_IGUAL = r'\+='
    t_VIRGULA = r','
    t_PONTO_VIRGULA = r';'
    t_LPAR = r'\('
    t_RPAR = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'

    t_ignore = " \t"

    def t_ID(self, t):
        r'(-)?[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reservadas.get(t.value, 'ID')  # Verificar palavras reservadas
        return t


    def t_NUMERO(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_STRING(self, t):
        r'\".*?\"'
        t.value = t.value[1:-1]
        return t

    def t_COMENTARIO_UMA_LINHA(self, t):
        r'\/\/.*'
        return None

    def t_COMENTARIO_MULTIPLAS_LINHAS(self, t):
        r'\/\*[\s\S]*?\*\/'
        t.lexer.lineno += t.value.count('\n')
        return None

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Caractere inválido: '{t.value[0]}'")
        t.lexer.skip(1)

    # Construir o lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def input(self, data):
        self.lexer.input(data)

    def token(self):
        return self.lexer.token()