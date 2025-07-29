import datetime

class SemanticMemorySystem:
    """Stores semantic fragments from conversations and events.

    存储介绍对话和事件的语义片段，方便后续查询。
    """

    def __init__(self):
        """Initialize an empty memory list."""
        self.memory = []  # 记忆列表：(时间戳，内容，其他元数)

    def store(self, text, **meta):
        """Store a new memory entry with optional metadata.

        存储一条记忆，可以传入额外的元数信息。
        """
        entry = {
            "time": datetime.datetime.utcnow().isoformat(),
            "text": text,
            "meta": meta,
        }
        self.memory.append(entry)

    def retrieve(self, keyword):
        """Return memories containing the keyword.

        从记忆中搜索包含指定关键字的条目。
        """
        return [m for m in self.memory if keyword in m["text"]]

    def recent(self, limit=5):
        """Return the most recent memories."""
        return self.memory[-limit:]
