class MachineNetwork:
    def __init__(self):
        # Dictionary to store machines and their connections
        self.machine_links = {}

    def add_machine(self, machine):
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, machine1, machine2):
        # Make sure both machines exist
        if machine1 not in self.machine_links:
            self.add_machine(machine1)
        if machine2 not in self.machine_links:
            self.add_machine(machine2)

        # Add connections in both directions
        if machine2 not in self.machine_links[machine1]:
            self.machine_links[machine1].append(machine2)

        if machine1 not in self.machine_links[machine2]:
            self.machine_links[machine2].append(machine1)

    def print_network(self):
        print("Machine Network:")
        for machine in self.machine_links:
            print(machine, "->", self.machine_links[machine])

    def print_connected_machines(self, machine):
        if machine in self.machine_links:
            print(machine, "is connected to:", self.machine_links[machine])
        else:
            print("Machine not found.")

    # <------------------------->
    # BFS METHOD
    # <------------------------->
    def bfs(self, start):
        # Check if start machine exists
        if start not in self.machine_links:
            print("Error: Machine not found in the network.")
            return []

        visited = []      # list to store visited machines
        queue = []        # list used as queue

        queue.append(start)
        visited.append(start)

        # Continue until queue is empty
        while len(queue) > 0:
            current = queue.pop(0)  # remove from front

            # Check neighbors
            for neighbor in self.machine_links[current]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        return visited


# Create the network
network = MachineNetwork()

network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

# Test BFS
print(network.bfs("Machine_A"))