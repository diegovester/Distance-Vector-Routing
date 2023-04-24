# Diego Vester
# 1001329342
# 04/23/2023
# CSE 4344-001

class Node:
    def __init__(self, receiver, cost):
        self.receiver = receiver
        self.cost = cost

    def __str__(self):
        return f"{self.receiver} {self.cost}"
    
    # reference: https://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes
    #def __eq__(self,other):
     #   if not isinstance(other, Node):
      #      return NotImplemented

       # return self.receiver == other.receiver and self.cost == other.cost
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    
    
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



# function to determine the current state of the network
def current_state(nodes):
    # COMPLETE
    # print the current state of the network
    # print the DV table for each node
    DV_state=[]
    for x in range(6):
        print(f'Node {x+1}')
        for link in nodes[x]:
            print(link)
            DV_state.append(link)
        #print('')
    return DV_state
    pass



# sending DV to Neighbors
# distance vector algorithm
# function to determine the next state of a specific node based on its neighboring nodes
def next_state(nodes, node):
    # COMPLETE
    neighboring_links = []
    # determine the next state of the network
    # use the Bellman-Ford equation
    # update the DV table for each node
    for link in nodes[node]:
        #print(link)
        for link2 in nodes[link.receiver-1]:
            #print(link2)
            node1_link = [link.receiver, link.cost]
            node2_link = [link2.receiver, link2.cost]
            new_link = [node2_link[0], node1_link[1]+node2_link[1]]
            #print(new_link)
            neighboring_links.append(new_link)
            #nodes[node].insert(new_link[0]-1, Node(new_link[0], new_link[1]))
    
                #node1_link = [2, 7]
                #node2_link = [3, 1]
                #new_link = [node2_link[0], node1_link[1]+node2_link[1]]
                #print(nodes[0].insert(new_link[0]-1, Node(new_link[0], new_link[1])))
    # return the next state of the network
    return neighboring_links
    pass

# duplicates may be created in the neighboring_links array
# duplicates would mess up the update_table function
def remove_duplicates(neighboring_links):
    new_links = []
    for link in neighboring_links:
        if link not in new_links:
            new_links.append(link)
    return new_links

def update_table(nodes, node):
    # INCOMPLETE
    # receive an update from another node
    neighboring_links = next_state(nodes, node)
    neighboring_links = remove_duplicates(neighboring_links)
    # update the DV table for the node
    # loop over neighboring_links 
    # if the node is in the DV table, and the new cost is less than the current, update the cost
    # if the node is not in the DV table, add the node and cost
    # if the node is in the DV table, and the new cost is greater than the current, do nothing

    temp_list = []
    for new_link in neighboring_links:
        for link in nodes[node]:
            if link.receiver == new_link[0]:
                if link.cost > new_link[1]:
                    link.cost = new_link[1]
                temp_list.append(new_link)
    
    clean_list = []
    for link in neighboring_links:
        if link not in temp_list:
            clean_list.append(link)
    
    for new_link in clean_list:
       nodes[node].insert(new_link[0]-1, Node(new_link[0], new_link[1]))

    # if the DV table has changed, return false
    pass

# function to check if the network is in a stable state
def stable_state(nodes):
    # INCOMPLETE
    # check if the network is in a stable state
    # if the network is in a stable state, return true
    # if the network is not in a stable state, return false
    pass

# function to run the distance vector algorithm
def run_algorithm(nodes):
    # INCOMPLETE
    x = 0
    total_time = f'___ Hop: #{x} ___'
    print(total_time)
    previous_state = current_state(nodes)
    # run the distance vector algorithm
    bool = True
    while(bool):
        print('')
        total_time = f'___ Hop: #{x+1} ___'
        print(total_time)
        for node in range(6):
            update_table(nodes, node)
        x += 1
        new_state = current_state(nodes)
        if new_state == previous_state:
            print("### stable ###")
            break
        else:
            previous_state = new_state
            print("### not stable ###")

        
    # if the network is not in a stable state, run the algorithm again
    # if the network is in a stable state, stop
    pass

        
# COMPLETE
# Select the input file
# Initial DV tables set up in GUI
# Runs algorithm correctly in single step mode - record DVs
# change a link cost and run from the previous state
# Systems detect a stable state
# runs algorithm without stopping - displays time
# Comments in code

# INCOMPLETE
# Writeup - include all elements discussed above

def main():
    network = read_network()
    nodes = initialize_tables(network)
    run_algorithm(nodes)
    

    



if __name__ == "__main__":
    main()