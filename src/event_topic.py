class EventTopic:
    """Simple in-memory simulation of an event-streaming topic."""

    def __init__(self, name):
        """Create an in-memory topic with a name and message buffer."""
        self.name = name
        self.messages = []

    def publish(self, event):
        """Append a single event to the topic."""
        self.messages.append(event)

    def get_messages(self):
        """Return a copy of the topic messages."""
        return list(self.messages)

    def clear(self):
        """Clear all buffered messages."""
        self.messages.clear()