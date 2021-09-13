import ast
import operator
import math

# Math operators dict
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}

# Math functions dict
math_functions = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'sqrt': math.sqrt,
    'abs': math.fabs
}

# Math constants dict
constants = {
    'pi': math.pi,
    'e': math.e
}


def get_expr():
    expr = input("Enter math expression or 'stop' to stop calculator: ")
    return expr


def parse_expr(expr):
    expr_tree = ast.parse(expr, mode='eval').body
    return expr_tree


def calc_expr(expr_tree):

    ast_types = {
        ast.Constant: 'float(expr_tree.value)',
        ast.Name: 'constants[expr_tree.id]',
        ast.UnaryOp: 'operators[type(expr_tree.op)](calc_expr(expr_tree.operand))',
        ast.BinOp: 'operators[type(expr_tree.op)](calc_expr(expr_tree.left), calc_expr(expr_tree.right))',
        ast.Call: 'math_functions[expr_tree.func.id](calc_expr(*expr_tree.args))'
    }

    if type(expr_tree) in ast_types:
        return eval(ast_types[type(expr_tree)])


def main():
    while True:
        try:
            expr = get_expr()

            if expr == 'stop':
                break

            expr_tree = parse_expr(expr)
            result = round(calc_expr(expr_tree), 2)

        except ZeroDivisionError:
            print('Can not divide by zero.')

        except (TypeError, ValueError):
            print('Wrong input! Calculator does not support strings. Please enter expression without braces!')

        except (KeyError, SyntaxError):
            print('Wrong input! Please, enter math expression to calculate.')

        except (OverflowError, MemoryError):
            print('Result too large.')

        else:
            print(result)


if __name__ == '__main__':
    main()
