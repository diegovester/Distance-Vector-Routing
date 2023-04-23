class Node:
    def __init__(self, receiver, cost):
        self.receiver = receiver
        self.cost = cost

    def __str__(self):
        return f"{self.receiver} {self.cost}"
    
    
# convert list of strings to a list of ints
def convert_to_ints(list):
    return [int(i) for i in list]


# function to read a plain text input file called input.txt
def read_file():
    file = open("input.txt", "r")
    print(file.read())

# The plain text input will describe the network
# Each line in the file will describe a link
# The line will have 3 numbers
# The numbers of the two nodes followed by the cost of the link
# For example, using numbers for the nodes instead of letters
def read_network():
    file = open("input.txt", "r")
    links = []
    for line in file:
        # split the line into three parts
        # the first number is the first node
        # the second number is the second node
        # the third number is the link
        parts = line.split()
        link_int = convert_to_ints(parts)
        
        # add the link to the array
        links.append(link_int)
    file.close()
    return links

def print_network(links):
    # print a table header
    print("Node 1\tNode 2\tCost")

    # print the links in a table
    for link in links:
        table_line = f'{link[0]}\t{link[1]}\t{link[2]}'
        print(table_line)

# function to initialize the distance vector table for a singular node
def initialize_table(sender, links):
    DV_table = []
    for link in links:
        if link[0] == sender:
            print(link[0], link[1], link[2])
            DV_table.append(Node(link[1], link[2]))
    return DV_table

# function to initialize a distance vector table for each node
def initialize_tables(links):
    nodes = []
    temp_DV_table = []
    for x in range(1,7):
        temp_DV_table.append(Node(x, 0))
        for link in links:
            if link[0] == x:
                temp_DV_table.append(Node(link[1], link[2]))
            

        nodes.append(temp_DV_table)
        #print(nodes)
        temp_DV_table = []
    return nodes

# function to determine if the network is in a stable state
def stable_state(nodes):
    # COMPLETE
    # check the DV table for each node
    # if the DV table has changed, return false
    # if the DV table has not changed, return true
    pass

# function to determine the current state of the network
def current_state(nodes):
    # COMPLETE
    # print the current state of the network
    # print the DV table for each node
    for x in range(6):
        print(f'Node {x+1}')
        for link in nodes[x]:
            print(link)
        print('')
    pass

# function to connect the nodes with each other using sockets when they need to

        
# COMPLETE
# Select the input file
# Initial DV tables set up in GUI

# INCOMPLETE
# Systems detect a stable state
# Runs algorithm correctly in single step mode - record DVs
# runs algorithm without stopping - displays time
# change a link cost and run from the previous state
# Writeup - include all elements discussed above
# Comments in code
def main():
    network = read_network()
    #print_network(network)
    nodes = initialize_tables(network)
    #print(nodes[0][1])
    current_state(nodes)
        
    

if __name__ == "__main__":
    main()