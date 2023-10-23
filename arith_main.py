from arith_lexer import ArithLexer
from arith_grammar import ArithGrammar
from arith_eval import ArithEval
from arith_c import write_to_c_file
def main():
    lexer = ArithLexer()
    parser = ArithGrammar()
    evaluator = ArithEval()

    # Construa o lexer e o parser
    lexer.build()
    parser.build()

    # Leia o programa a partir do arquivo
    with open('entrada.ea', 'r') as file:
        program = file.read()

    output_file = 'output.c'
    write_to_c_file(program, output_file)

    # Analise o programa
    ast = parser.parse(program)
    print("AST:", ast)

    # Avalie o programa
    result = evaluator.evaluate(ast)

    # Imprima o resultado
    print(f"Resultado: {result}")

if __name__ == "__main__":
    main()
