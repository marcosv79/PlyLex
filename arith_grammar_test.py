from arith_grammar import ArithGrammar
from pprint import PrettyPrinter
from arith_eval import ArithEval

pp = PrettyPrinter(sort_dicts=False)
evaluator = ArithEval()
ag = ArithGrammar()
ag.build()

exemplos = [ # exemplos a avaliar de forma independente... 
            "VAR x = 2;",
            "x++",
            "x * 4"
            ]
for frase in exemplos:
    print(f"----------------------")
    print(f"--- frase '{frase}'")
    ast = ag.parse(frase)
    result = evaluator.evaluate(ast)  
    print(f"Resultado: {result}")
