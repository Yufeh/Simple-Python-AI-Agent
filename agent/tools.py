"""
tools.py
Simple "tools" the agent can call to perform real actions, rather
than just generating text.

COMMIT 3 (on feature/tools branch): Adds two tools:
  - calculate(): evaluates basic arithmetic expressions safely
  - get_time(): returns the current time

This is a simplified version of the "function calling" / "tool use"
pattern used by real-world AI agents (e.g. Bedrock Agents, OpenAI
function calling, MCP tools).
"""

import datetime
import operator
import re

# Only allow these operators -- avoids using eval() on arbitrary input,
# which would be a security risk if this ever took untrusted input.
_ALLOWED_OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

_EXPR_PATTERN = re.compile(r"^\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*$")


def calculate(expression):
    """
    Evaluate a simple two-operand arithmetic expression, e.g. "4 + 5".
    Returns a string result or an error message -- never raises.
    """
    match = _EXPR_PATTERN.match(expression)
    if not match:
        return "Sorry, I can only handle simple expressions like '4 + 5'."

    left_str, op, right_str = match.groups()
    left = float(left_str)
    right = float(right_str)

    if op == "/" and right == 0:
        return "Error: division by zero."

    result = _ALLOWED_OPERATORS[op](left, right)

    # Show whole numbers without a trailing .0
    if result == int(result):
        result = int(result)

    return f"{expression.strip()} = {result}"


def get_time():
    """Return the current time as a friendly string."""
    now = datetime.datetime.now()
    return now.strftime("It is currently %H:%M:%S on %A, %d %B %Y.")


# A simple registry so the agent can look up tools by name.
AVAILABLE_TOOLS = {
    "calculate": calculate,
    "get_time": get_time,
}