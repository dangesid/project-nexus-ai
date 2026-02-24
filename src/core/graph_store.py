from typing import Dict, List

class GraphStore:
    """
    Lightweight in-memory graph store

    Responsibilities:
    - Store relationships between entitites
    - Retrieve neighbors for recommendation expansion
    """

    def __init__(self):
        self._graph: Dict[str, List[str]] = {}

    def add_edge(self, source: str, target: str, action: str):
        """ Add directed edge"""
        if source not in self._graph:
            self._graph[source] = []

        self._graph[source].append((target, action))
       
        # Reverse edge (optional but useful)
        if target not in self._graph:
            self._graph[target] = []

        self._graph[target].append((source, action))
        print(f"[GraphStore] Edge added: {source} --> {target}")

    # Neighbor Lookup 

    def get_neighbors(self, node:str):
        """Return Connected nodes """
        return self._graph.get(node, [])
    