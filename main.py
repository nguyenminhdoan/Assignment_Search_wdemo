# Run test cases
from QueueBFS import BFS_Minh

if __name__ == "__main__":
    from GraphData import connections

    print("Case 1: Dolly to Minh")
    BFS_Minh(connections, 'Dolly', 'Minh')

    print("\nCase 2: George to Bob")
    BFS_Minh(connections, 'George', 'Bob')