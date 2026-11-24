from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class BFS(BaseSearch):
    def search(self, initial: State) -> SearchResult:
        frontier = deque([initial])
        visited = {initial}
        expanded = 0
        generated = 1
        max_frontier = 1

        while frontier:
            current = frontier.popleft()
            if current.is_goal:
                return SearchResult(current, expanded, generated, max_frontier, current.cost)
            expanded += 1
            for child in current.neighbors():
                if child not in visited:
                    visited.add(child)
                    frontier.append(child)
                    generated += 1
            max_frontier = max(max_frontier, len(frontier))

        return SearchResult(None, expanded, generated, max_frontier, 0)
