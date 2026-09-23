import ast
import operator

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}


def calculate(expression: str):

    def evaluate(node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Invalid number")

        if isinstance(node, ast.BinOp):
            operation = OPERATORS.get(type(node.op))
            if not operation:
                raise ValueError("Operator not allowed")

            return operation(
                evaluate(node.left),
                evaluate(node.right)
            )

        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -evaluate(node.operand)

        raise ValueError("Invalid expression")

    tree = ast.parse(expression, mode="eval")

    return evaluate(tree.body)