'''
@author: Devangini Patel
'''

from Node import Node
from State import State
from collections import deque

def BFS_Minh(graph, start, goal):
    """
    This function performs BFS search using a queue
    """
    # Error: Start/goal not in graph
    if start not in graph:
        print(f"Error: '{start}' does not exist in the graph.")
        return
    if goal not in graph:
        print(f"Error: '{goal}' does not exist in the graph.")
        return

    #create queue
    queue = deque([]) 
    #since it is a graph, we create visited list
    visited = set()
    #create root node
    initialState = State(start, graph)
    root = Node(initialState)
    #add to queue and visited list
    queue.append(root)    
    # visited.append(root.state.name)
    visited.add(start)

    found = False

    # check if there is something in queue to dequeue
    while queue:
        current_node = queue.popleft()
        print(f"-- Dequeued: {current_node.state.name}")

        # Check if goal is reached
        if current_node.state.checkGoalState(goal):
            print("\nPath found!")
            current_node.printPath()
            found = True
            break

        # Expand children
        for neighbor in current_node.state.successorFunction():
            if neighbor not in visited:
                visited.add(neighbor)
                child_node = Node(State(neighbor, graph))
                current_node.addChild(child_node)
                queue.append(child_node)

    if not found:
        print("\nApology: No introduction path exists.")

    # Print the tree
    print("\nTraversal Tree:")
    root.printTree()
    
