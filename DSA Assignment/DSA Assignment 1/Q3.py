def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n-1, auxiliary, source, destination)


# Example call
tower_of_hanoi(3, 'A', 'B', 'C')

# Trace for N = 3
    
# Call:
# tower_of_hanoi(3, A, B, C)
# Steps:
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C
# Total Moves = 7

# Time Complexity

# Recurrence relation:
# T(n) = 2T(n-1) + 1
# Solving this gives:
# T(n) = 2ⁿ − 1
# Therefore,
# Time Complexity = O(2ⁿ)