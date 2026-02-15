from typing import Any, Dict

class MemoryStore:
    """
    Simple in memory shared for agents
    Act as a lightweight central memory.

    Responsibilities:
     - Save agent processed data
     - Retrive data by key

    """

    def __init__(self):
        self._store: Dict[str, Any] = {}  # Correct internal store

    def save(self, key: str, value: Any):
        """Save data to memory store"""
        self._store[key] = value
        print(f"[MemoryStore] Saved data for key: {key}")

    def get(self, key: str) -> Any:
        """Retrieve data by key"""
        return self._store.get(key)

    def set(self, key: str, value: Any) -> None:
        """Set value directly"""
        self._store[key] = value

    def update_list(self, key: str, value: Any) -> None:
        """Append value to list at key"""
        if key not in self._store:
            self._store[key] = []
        self._store[key].append(value)

    def clear(self) -> None:
        """Clear all memory"""
        self._store.clear()