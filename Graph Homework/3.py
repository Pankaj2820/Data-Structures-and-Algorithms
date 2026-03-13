class MachineNetwork:
    def __init__(self):
        self.machine_links = {}

    def add_machine(self, machine):
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        if m1 not in self.machine_links:
            self.add_machine(m1)
        if m2 not in self.machine_links:
            self.add_machine(m2)

        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)
        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    # -------- DFS --------
    def dfs(self, start):
        if start not in self.machine_links:
            print("Machine not found.")
            return []

        visited = []
        stack = [start]

        while stack:
            current = stack.pop()   # remove from end

            if current not in visited:
                visited.append(current)

                # add neighbors to stack
                for neighbor in self.machine_links[current]:
                    stack.append(neighbor)

        return visited


# Create network
network = MachineNetwork()

network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

# Test DFS
print(network.dfs("Machine_A"))