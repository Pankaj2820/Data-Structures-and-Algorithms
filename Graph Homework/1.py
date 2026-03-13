class MachineNetwork:
    def __init__(self):
        # This dictionary will store each machine and its connected machines
        self.machine_links = {}

    def add_machine(self, machine):
        # Add the machine only if it does not already exist
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, machine1, machine2):
        # Make sure both machines exist in the network
        if machine1 not in self.machine_links:
            self.add_machine(machine1)
        if machine2 not in self.machine_links:
            self.add_machine(machine2)

        # Connect both machines (two-way connection)
        if machine2 not in self.machine_links[machine1]:
            self.machine_links[machine1].append(machine2)

        if machine1 not in self.machine_links[machine2]:
            self.machine_links[machine2].append(machine1)

    def print_network(self):
        print("Machine Network:")
        for machine in self.machine_links:
            print(machine, "is connected to", self.machine_links[machine])

    def print_connected_machines(self, machine):
        if machine in self.machine_links:
            print(machine, "is directly connected to:", self.machine_links[machine])
        else:
            print("Machine not found in the network.")


# Create the network
network = MachineNetwork()

# Create the required links
network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

# Print everything
network.print_network()

print()  # just for spacing
network.print_connected_machines("Machine_C")