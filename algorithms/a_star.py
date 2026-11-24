import heapq
from itertools import count
from puzzle.base_search import BaseSearch
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult


class AStar(BaseSearch):
    def heuristic(self, state: State) -> int:
        """Distância Manhattan total das peças (o espaço vazio é ignorado)."""
        total = 0
        for index, tile in enumerate(state.tiles):
            if tile == 0:
                continue
            goal_index = GOAL_STATE.index(tile)
            row, col = divmod(index, 3)
            goal_row, goal_col = divmod(goal_index, 3)
            total += abs(row - goal_row) + abs(col - goal_col)
        return total



    def search(self, initial: State) -> SearchResult:
        sequence = count()
        frontier = [(self.heuristic(initial), next(sequence), initial)]
        best_cost = {initial: 0}
        expanded = 0
        generated = 1
        max_frontier = 1

        while frontier:
            _, _, current = heapq.heappop(frontier)
            if current.cost != best_cost.get(current):
                continue
            if current.is_goal:
                return SearchResult(current, expanded, generated, max_frontier, current.cost)
            expanded += 1
            for child in current.neighbors():
                if child.cost < best_cost.get(child, float("inf")):
                    best_cost[child] = child.cost
                    priority = child.cost + self.heuristic(child)
                    heapq.heappush(frontier, (priority, next(sequence), child))
                    generated += 1
            max_frontier = max(max_frontier, len(frontier))

        return SearchResult(None, expanded, generated, max_frontier, 0)
