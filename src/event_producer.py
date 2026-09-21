try:
    from src.event_topic import EventTopic
except ModuleNotFoundError:  # pragma: no cover - script execution fallback
    from event_topic import EventTopic


class EventProducer:
    """Publishes anomaly events to an in-memory topic."""

    def __init__(self, topic: EventTopic):
        """Create a producer bound to a specific event topic."""
        self.topic = topic

    def publish(self, event):
        """Publish an event if it exists and return whether it succeeded."""
        if not event:
            return False

        self.topic.publish(event)
        return True