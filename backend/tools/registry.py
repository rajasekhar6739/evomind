from tools.calculator import calculate


TOOLS = {
    "calculator": {
        "name": "Calculator",
        "description": "Performs mathematical calculations",
        "function": calculate
    }
}


def list_tools():

    return [
        {
            "name": name,
            "description": tool["description"]
        }
        for name, tool in TOOLS.items()
    ]


def execute_tool(tool_name: str, tool_input: str):

    if tool_name not in TOOLS:
        return {
            "status": "error",
            "message": f"Tool '{tool_name}' not found"
        }

    try:
        result = TOOLS[tool_name]["function"](tool_input)

        return {
            "status": "success",
            "tool": tool_name,
            "result": result
        }

    except Exception as error:

        return {
            "status": "error",
            "tool": tool_name,
            "message": str(error)
        }