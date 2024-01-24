#### gredy depth first search


index = 0
cost = 1


def depth_first_search(graph):
    num_nodes = len(graph)
    path_stack = [0]
    temp_stack = []
    path = []

    while path_stack:
        print("trenutni stek" + str(path_stack))
        current_node = path_stack.pop()
        path.append(current_node)

        print("trenutni put" + str(path))
        if len(path) == num_nodes:
            path.append(0)
            print("trenutni stek" + str(path_stack))
            print("Depth first: "+"Optimalni put: " + str(path))
            return path

        children = graph[current_node]

        for i in range(0, len(children)):
            if children[i] != 0 and i not in path:
                temp_stack.append([i, children[i]])
           
        print("nesortirani" + str(temp_stack))
        temp_stack.sort(key=lambda x: (x[cost], x[index]))
        print("sortirani" + str(temp_stack))

        for i in range(len(temp_stack) - 1, -1, -1):
            path_stack.append(temp_stack[i][index])
        temp_stack = []




####Brute force

def brute_force_tsp(matrix):
    num_nodes = len(matrix)

    
    min_cost = float('inf')
    min_cost_path = []

    all_nodes = list(range(1, num_nodes))  
    all_permutations = generate_permutations(all_nodes)
     
    for path in all_permutations:
        current_cost = calculate_total_distance(path,matrix)
        print(path,current_cost)
        
        if current_cost < min_cost:
            min_cost = current_cost
            min_cost_path = path
    print(min_cost_path)
    return min_cost_path



def calculate_total_distance(path,matrix):
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += matrix[path[i]][path[i + 1]]
        
        return total_distance

def generate_permutations(nodes):
        permutations = []

        

        permute([0], nodes,permutations)
       
        return permutations


def permute(current_path, remaining_nodes,permutations):
            if not remaining_nodes:
                permutations.append(current_path + [current_path[0]]) 
             
                return

            for i in range(len(remaining_nodes)):
              
                new_node = remaining_nodes[i]
                updated_path = current_path + [new_node]
                updated_remaining_nodes = [node for node in remaining_nodes if node != new_node]
                permute(updated_path, updated_remaining_nodes,permutations)


#### Branch and bound
import json
class Node:
    def __init__(self, current_node, cost, path):
        self.current_node = current_node
        self.cost = cost
        self.path = path


    def to_dict(self):
        return {'current_node': self.current_node, 'cost': self.cost, 'path': self.path}


def branch_and_bound(graph):
    num_of_nodes = len(graph)
    path_queue = [Node(0, 0, [0])]

    while path_queue:
        #print("Path queue:", json.dumps([node.to_dict() for node in path_queue]))
        current_node = path_queue.pop(0)

        #print("Current node:"+str(current_node.current_node)+"Current cost:"+str(current_node.cost)+ "Current path:"+str(current_node.path))

        if len(current_node.path) == num_of_nodes + 1:
            
            print("BranchAndBound"+"Optimal node: "+str(current_node.current_node)+"Optimal cost: "+str(current_node.cost)+"Optimal path: "+
                  str(current_node.path))
                  
            return current_node.path

        children = graph[current_node.current_node]

        for i in range(len(children)):
            if children[i] != 0 and i not in current_node.path and len(current_node.path) < len(children):
                new_path = current_node.path[:]
                new_path.append(i)
                new_cost = current_node.cost + children[i]
                new_node = Node(i, new_cost, new_path)
                path_queue.append(new_node)

            if len(current_node.path) == len(children):
                new_path = current_node.path[:]
                new_path.append(0)
                new_cost = current_node.cost + children[0]
                new_node = Node(0, new_cost, new_path)
                path_queue.append(new_node)
                break

        path_queue.sort(key=lambda x: (x.cost,-len(x.path), x.current_node))
        
        
        
 
####A star
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import json
class Node2:
    def __init__(self, current_node, cost, heuristics, total_cost, path):
        self.current_node = current_node
        self.cost = cost
        self.heuristics = heuristics
        self.total_cost = total_cost
        self.path = path
    def to_dict(self):
        return {'current_node': self.current_node, 'cost': self.cost,'heuristcis':self.heuristics,'total_cost':self.total_cost,'path': self.path}
    
    
def A_star(graph):
    num_of_nodes = len(graph)
    path_queue = [Node2(0, 0, 0, 0, [0])]
    MST_cost = 0
    Temp = []

    while path_queue:
        #print("Path queue:", json.dumps([node.to_dict() for node in path_queue]))
        current_node = path_queue.pop(0)
       

        #print("Current node:", current_node.current_node, "Current cost:", current_node.cost,
              #"Heuristic:", current_node.heuristics, "Total cost:", current_node.total_cost,
              #"Current path:", current_node.path)

        if len(current_node.path) == num_of_nodes + 1:
            print("AStar"+"Optimal node:", current_node.current_node, "Optimal cost:", current_node.cost,
                  "Optimal heuristic:", current_node.heuristics, "Optimal total cost:", current_node.total_cost,
                  "Optimal path:", current_node.path)
            return current_node.path

        children = graph[current_node.current_node]
        Temp = make_matrix_for_kruskal(graph)
        #print(Temp)
        k = 0

        for k in range(1, len(current_node.path)):
            Temp = [item for item in Temp if  (item[0] != current_node.path[k] and item[1] != current_node.path[k])]

        #print("Temp:", k, "||", Temp)

        MST_cost = kruskal_algo(len(graph), Temp)

        for i in range(len(children)):
            if children[i] != 0 and i not in current_node.path and len(current_node.path) < len(children):
                new_path = current_node.path[:]
                new_path.append(i)
                new_cost = current_node.cost + children[i]
                total_cost = new_cost + MST_cost
                new_node = Node2(i, new_cost, MST_cost, total_cost, new_path)
                path_queue.append(new_node)

            if len(current_node.path) == len(children):
                new_path = current_node.path[:]
                new_path.append(0)
                new_cost = current_node.cost + children[0]
                total_cost = new_cost + MST_cost
                new_node = Node2(0, new_cost, MST_cost, total_cost, new_path)
                path_queue.append(new_node)
                break

        path_queue.sort(key=lambda x: (x.total_cost, -len(x.path), x.current_node))


def make_set(parent, rank, n):
    for i in range(n):
        parent[i] = i
        rank[i] = 0


def find_parent(parent, component):
    if parent[component] == component:
        return component

    parent[component] = find_parent(parent, parent[component])
    return parent[component]

    

def union_set(u, v, parent, rank, n):
    u = find_parent(parent, u)
    v = find_parent(parent, v)

    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[u] > rank[v]:
        parent[v] = u
    else:
        parent[v] = u
        rank[u] += 1


def kruskal_algo(n, edge):
    edge.sort(key=lambda x: x[2])
    parent = [0] * n
    rank = [0] * n
    make_set(parent, rank, n)
    min_cost = 0

    for i in range(len(edge)):
        v1 = find_parent(parent, edge[i][0])
        v2 = find_parent(parent, edge[i][1])
        wt = edge[i][2]

        if v1 != v2:
            union_set(v1, v2, parent, rank, n)
            min_cost += wt
            #print(edge[i][0], "--", edge[i][1], "==", wt)

    #print("Heuristic:", min_cost)
    return min_cost


def make_matrix_for_kruskal(matrix):
    num_nodes = len(matrix)
    visited = [False] * num_nodes
    new_matrix = []

    for i in range(num_nodes):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0 and not visited[j]:
                new_matrix.append([i, j, matrix[i][j]])

        visited[i] = True

    return new_matrix

        
        
  
    