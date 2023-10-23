class ArithEval:
    symbols = {}

    operators = {
        "MAIS": lambda args: args[0] + args[1],
        "MENOS": lambda args: args[0] - args[1],
        "MULT": lambda args: args[0] * args[1],
        "DIVISAO": lambda args: args[0] / args[1] if args[1] != 0 else float('inf'),
        "INCREMENT": lambda args: args[0] + 1,
    }

    @staticmethod
    def evaluate(ast):
        if type(ast) is int:
            return ast
        if type(ast) is dict:
            op = ast["op"]
            args = ast['args']
            if op == "VAR":
                for var_name, value in args:
                    ArithEval.symbols[var_name] = ArithEval.evaluate(value)
                return ArithEval.symbols
            elif op == "ESCREVER":
                evaluated_args = [ArithEval.evaluate(a) for a in args]
                return " ".join(str(arg) for arg in evaluated_args)
            elif op in ArithEval.operators:
                evaluated_args = [ArithEval.evaluate(a) for a in args]
                func = ArithEval.operators[op]
                return func(evaluated_args)
            else:
                raise Exception(f"Unknown operator {op}")
        if type(ast) is str:
            return ast
        raise Exception(f"Unknown AST type")

    @staticmethod
    def _eval_operator(ast):
        if 'op' in ast:
            op = ast["op"]
            args = ast['args']
            if op in ArithEval.operators:
                args = [ArithEval.evaluate(a) for a in args]
                func = ArithEval.operators[op]
                return func(args)
            else:
                raise Exception(f"Unknown operator {op}")
        raise Exception('Undefined AST')
