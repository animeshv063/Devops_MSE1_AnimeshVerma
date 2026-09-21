try:
    from src.event_topic import EventTopic
except ModuleNotFoundError:  # pragma: no cover - script execution fallback
    from event_topic import EventTopic


class EventConsumer:
    """Consumes events from an in-memory topic."""

    def __init__(self, topic: EventTopic):
        """Create a consumer bound to a specific event topic."""
        self.topic = topic

    def consume(self):
        """Return all messages currently stored in the topic."""
        return self.topic.get_messages()