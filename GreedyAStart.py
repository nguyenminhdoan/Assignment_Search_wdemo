import heapq
from GraphData import connections


def uniform_cost_search(graph, start, goal):
    """ Implements Uniform Cost Search (UCS) """
    if start not in graph or goal not in graph:
        print(f"Error: '{start}' or '{goal}' not found in the graph.")
        return

    priority_queue = []  # Min-heap for UCS
    heapq.heappush(priority_queue, (0, start, [start]))  # (cost, node, path)
    visited = set()
    nodes_expanded = 0

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)
        nodes_expanded += 1

        if current == goal:
            print("\nUniform Cost Search Result:")
            print("Shortest Path:", " -> ".join(path))
            print("Total Cost:", cost)
            print("Nodes Expanded:", nodes_expanded)
            return

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + 1, neighbor, path + [neighbor]))

    print("No path found.")


# Example Graph with Weights (Modify as Needed)
# Run UCS
uniform_cost_search(connections, 'Dolly', 'Minh')