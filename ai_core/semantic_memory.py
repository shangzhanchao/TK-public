import datetime

class SemanticMemorySystem:
    """Stores semantic fragments from conversations and events."""

    def __init__(self):
        self.memory = []  # list of (timestamp, text, meta)

    def store(self, text, **meta):
        entry = {
            "time": datetime.datetime.utcnow().isoformat(),
            "text": text,
            "meta": meta,
        }
        self.memory.append(entry)

    def retrieve(self, keyword):
        return [m for m in self.memory if keyword in m["text"]]

    def recent(self, limit=5):
        return self.memory[-limit:]
