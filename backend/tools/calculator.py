import ast
import operator
import re

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}


def calculate(expression: str):

    if not expression or not expression.strip():
        raise ValueError("Expression cannot be empty")

    expression = expression.lower().strip()

    # Remove common calculator words
    remove_words = [
        "calculate",
        "calculator",
        "compute",
        "what is",
        "what's",
        "please",
    ]

    for word in remove_words:
        expression = expression.replace(word, "")

    # Convert natural language operators
    expression = expression.replace("multiplied by", "*")
    expression = expression.replace("multiply", "*")
    expression = expression.replace("times", "*")

    expression = expression.replace("divided by", "/")
    expression = expression.replace("divide", "/")

    expression = expression.replace("plus", "+")
    expression = expression.replace("minus", "-")

    expression = expression.strip()

    # Keep only a mathematical expression
    match = re.search(r"[-+*/%().\d\s]+$", expression)

    if not match:
        raise ValueError("Invalid mathematical expression")

    expression = match.group(0).strip()

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

        if isinstance(node, ast.UnaryOp):

            if isinstance(node.op, ast.USub):
                return -evaluate(node.operand)

            if isinstance(node.op, ast.UAdd):
                return evaluate(node.operand)

        raise ValueError("Invalid expression")

    tree = ast.parse(expression, mode="eval")

    return evaluate(tree.body)
