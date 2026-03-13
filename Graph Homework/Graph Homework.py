
# Chapter 7 Homework Exercises Help

class MachineNetwork:
    def __init__(self):
        # key = machine, value = list of connected machines
        self.machine_links = {}

    def add_machine(self, machine):
        # TODO: add machine if it does not exist
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        # TODO:
        # 1. add machines if missing
        # 2. add link in both directions
        if m1 not in self.machine_links:
            self.add_machine(m1)
        if m2 not in self.machine_links:
            self.add_machine(m2)

        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)

        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def print_network(self):
        # TODO: print all machines and their links
        for machine in self.machine_links:
            print(machine, "->", self.machine_links[machine])

    def print_connected_machines(self, machine):
        # TODO: print machines directly connected to 'machine'
        if machine in self.machine_links:
            print(machine, "is connected to:", self.machine_links[machine])
        else:
            print("Machine not found.")

    def bfs(self, start):
        # TODO: implement Breadth-First Search using a list as a queue
        if start not in self.machine_links:
            print("Machine not found.")
            return []

        visited = []
        queue = [start]
        visited.append(start)

        while queue:
            current = queue.pop(0)
            for neighbor in self.machine_links[current]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        return visited

    def dfs(self, start):
        # TODO: implement Depth-First Search using a list as a stack
        if start not in self.machine_links:
            print("Machine not found.")
            return []

        visited = []
        stack = [start]

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                for neighbor in self.machine_links[current]:
                    stack.append(neighbor)

        return visited


# Testing the code:
network = MachineNetwork()

network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

network.print_network()
print()

network.print_connected_machines("Machine_C")
print()

print("BFS from Machine_A:", network.bfs("Machine_A"))
print("DFS from Machine_A:", network.dfs("Machine_A"))