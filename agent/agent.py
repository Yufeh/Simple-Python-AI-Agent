"""
agent.py
The main entry point for our simple AI agent.

COMMIT 5 (on feature/cli-polish branch): Final polish pass for v1.0.0.
Adds a 'help' command, graceful handling of empty/unexpected input,
and friendlier startup messaging. This is the last commit in our
5-commit teaching history.
"""

from memory import Memory
from tools import calculate, get_time
from logger import log_turn

VERSION = "1.0.0"


def greet():
    print("=" * 50)
    print(f"  Simple AI Agent  (v{VERSION})")
    print("=" * 50)
    print("Try: 'calc 4 + 5'  or  'what time is it'  or  'help'")
    print("Type 'exit' to quit.\n")


def show_help():
    return (
        "Available commands:\n"
        "  calc <expr>   e.g. 'calc 12 * 4'\n"
        "  time          ask what time it is\n"
        "  help          show this message\n"
        "  exit / quit   end the session"
    )


def generate_response(user_input):
    """
    Routing logic: look at the user's input and decide whether to
    call a tool, show help, or fall back to a generic response.
    Handles empty input gracefully instead of crashing.
    """
    if not user_input:
        return "I didn't catch that -- try typing 'help' to see what I can do."

    lowered = user_input.lower().strip()

    if lowered == "help":
        return show_help()

    if lowered.startswith("calc "):
        expression = user_input[5:]
        return calculate(expression)

    if "time" in lowered:
        return get_time()

    return "(not implemented yet -- try 'help' to see available commands)"


def run():
    greet()
    memory = Memory()

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAgent: Session interrupted. Goodbye!")
            break

        memory.add("user", user_input)
        log_turn("user", user_input)

        if user_input.lower() in ("exit", "quit"):
            farewell = f"Goodbye! We had {memory.turn_count()} turns this session."
            log_turn("agent", farewell)
            print(f"Agent: {farewell}")
            break

        response = generate_response(user_input)
        memory.add("agent", response)
        log_turn("agent", response)
        print(f"Agent: {response}")


if __name__ == "__main__":
    run()