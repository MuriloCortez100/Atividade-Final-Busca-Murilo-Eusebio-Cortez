from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):
    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        frontier = [initial]
        best_depth = {initial: 0}
        expanded = 0
        generated = 1
        max_frontier = 1

        while frontier:
            current = frontier.pop()
            if current.is_goal:
                return SearchResult(current, expanded, generated, max_frontier, current.cost)
            if current.cost >= self.depth_limit:
                continue
            expanded += 1
            # Reverse para que a ordem natural (UP, DOWN, LEFT, RIGHT) seja
            # preservada na exploração quando os filhos são empilhados.
            for child in reversed(current.neighbors()):
                depth = child.cost
                if depth <= self.depth_limit and (child not in best_depth or depth < best_depth[child]):
                    best_depth[child] = depth
                    frontier.append(child)
                    generated += 1
            max_frontier = max(max_frontier, len(frontier))

        return SearchResult(None, expanded, generated, max_frontier, 0)
