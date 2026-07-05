Simple Python AI Agent
A minimal, dependency-light AI agent built step by step to teach Git fundamentals.

What this agent does
A command-line agent that can:

Hold a conversation loop with a user
Use simple "tools" (calculator, time lookup) when asked
Remember conversation history for the session
Log every interaction to a file
Project structure
agent/
  agent.py        # main entry point
  tools.py        # tool functions the agent can call
  memory.py       # conversation history management
  requirements.txt
README.md
Status
v1.0.0 - Complete. The agent supports a conversation loop, in-memory history, two tools (calculator and clock), persistent file logging, a help command, and graceful error handling.

Built across 5 commits to demonstrate the Git lifecycle (add, commit, push, pull, merge) and feature branching:

Initial commit -- project skeleton
Add Memory module
Add tools (feature/tools branch -> fast-forward merge)
Add file logging (feature/logging branch -> 3-way merge)
CLI polish pass (feature/cli-polish branch -> this release)