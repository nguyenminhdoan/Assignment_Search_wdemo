import heapq


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
        print(f"Expanding: {priority_queue}")
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


def greedy_best_first_search(graph, start, goal, heuristic):
    """ Implements Greedy Best-First Search """
    if start not in graph or goal not in graph:
        print(f"Error: '{start}' or '{goal}' not found in the graph.")
        return

    priority_queue = []  # Min-heap for Greedy BFS
    heapq.heappush(priority_queue, (heuristic[start], start, [start], 0))
    visited = set()
    nodes_expanded = 0

    while priority_queue:
        print(f"Expanding: {priority_queue}")
        _, current, path, cost = heapq.heappop(priority_queue) if len(priority_queue[0]) == 4 else (
        *heapq.heappop(priority_queue), 0)
        nodes_expanded += 1

        if current == goal:
            print("Greedy Best-First Search Result:")
            print("Total Cost:", cost)
            print("Shortest Path:", " -> ".join(path))
            print("Nodes Expanded:", nodes_expanded)
            return

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue,
                                   (heuristic[neighbor], neighbor, path + [neighbor], cost + graph[current][neighbor]))

    print("No path found.")


def a_star_search(graph, start, goal, heuristic):
    """ Implements A* Search """
    if start not in graph or goal not in graph:
        print(f"Error: '{start}' or '{goal}' not found in the graph.")
        return

    priority_queue = []  # Min-heap for A*
    heapq.heappush(priority_queue, (0 + heuristic[start], 0, start, [start]))  # (f(n), g(n), node, path)
    visited = set()
    nodes_expanded = 0

    while priority_queue:
        print(f"Expanding: {priority_queue}")
        f, cost, current, path = heapq.heappop(priority_queue)
        nodes_expanded += 1

        if current == goal:
            print("\nA* Search Result:")
            print("Shortest Path:", " -> ".join(path))
            print("Total Cost:", cost)
            print("Nodes Expanded:", nodes_expanded)
            return

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    g = cost + 1
                    h = heuristic[neighbor]
                    heapq.heappush(priority_queue, (g + h, g, neighbor, path + [neighbor]))

    print("No path found.")


# Example Graph
graph = {
    "Bus Stop": {"Library": 2},
    "Library": {"Bus Stop": 2, "Student Center": 2, "Car Park": 5},
    "Student Center": {"Library": 1.2, "Theater": 1.4, "Store": 4},
    "Theater": {"Sports Center": 2, "Student Center": 1.4},
    "Sports Center": {"Library": 4, "Theater": 2, "Store": 1.4},
    "Car Park": {"Library": 5, "Maths Building": 4.2, "Store": 5},
    "Store": {"Sports Center": 1.4, "Library": 4, "Car Park": 5, "Canteen": 3},
    "Maths Building": {"Car Park": 4.2, "Canteen": 2},
    "Canteen": {"Maths Building": 2, "Store": 3, "AI Lab": 1},
    "AI Lab": {"Canteen": 1}
}

# Example Heuristic Function for Greedy & A* (Modify as Needed)
heuristic = {
    "Bus Stop": 8,
    "Library": 6,
    "Student Center": 5,
    "Theater": 4,
    "Sports Center": 3,
    "Car Park": 6,
    "Store": 2,
    "Maths Building": 3,
    "Canteen": 1,
    "AI Lab": 0  # Goal node
}

# Run Search Algorithms
print("\nRunning Uniform Cost Search (UCS) with Updated Graph:")
uniform_cost_search(graph, "Bus Stop", "AI Lab")

print("\nRunning Greedy Best-First Search with Updated Graph:")
greedy_best_first_search(graph, "Bus Stop", "AI Lab", heuristic)

print("\nRunning A* Search with Updated Graph:")
a_star_search(graph, "Bus Stop", "AI Lab", heuristic)

# Analysis:
print("\nAnalysis of Results:")
print("- UCS explores nodes in cost order, ensuring optimality but can expand many nodes.")
print("- Greedy Best-First Search expands fewer nodes but may not find the best path.")
print("- A* balances both by considering path cost and heuristic, usually performing best.")
