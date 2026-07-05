"""
memory.py
Handles conversation history for the agent.

COMMIT 2: Adds simple in-memory storage of the conversation so the
agent can later use past turns for context (e.g. when summarizing
or reasoning about what's already been said).
"""


class Memory:
    """Stores a session's conversation as a list of (speaker, text) turns."""

    def __init__(self):
        self.history = []

    def add(self, speaker, text):
        """Record one turn of the conversation."""
        self.history.append((speaker, text))

    def get_history(self):
        """Return the full conversation history."""
        return self.history

    def last_user_message(self):
        """Return the most recent message sent by the user, if any."""
        for speaker, text in reversed(self.history):
            if speaker == "user":
                return text
        return None

    def turn_count(self):
        """Return how many total turns have happened (user + agent)."""
        return len(self.history)

    def clear(self):
        """Wipe the conversation history."""
        self.history = []