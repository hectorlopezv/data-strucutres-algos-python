#Graoqhl structures 
import sys
from collections import deque
graphq = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": []

}
def depth_first_values_iteration(graphq, source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbor in graphq[current]:
            stack.append(neighbor)


def depth_first_values_recursion(graphq, source):
    print(source)
    for neighbor in graphq[source]:
        depth_first_values_recursion(graphq, neighbor)

def depth_first_values_recursion(graphq, source, visited):
    if source in visited:
        return
    print(source)
    visited.add(source)
    for neighbor in graphq[source]:
        depth_first_values_recursion(graphq, neighbor)      
def breath_first_values_iteration(graphq, source):
    queuq = [source]
    while len(queuq) > 0:
        current = queuq.pop(0)
        print(current)
        for neighbor in graphq[current]:
            queuq.append(neighbor)

def has_path(source, destination):
    queuq = [source]
    while len(queuq)> 0:
        current = queuq.pop(0)
        for neighbor in graphq[current]:
            queuq.append(neighbor)
    return False
def has_path_recursive_way(gtapqh, source, destination):

    if source == destination:
        return True
    for neigh in gtapqh[source]:
        res = has_path_recursive_way(gtapqh, neigh, destination)
        if res:
            return True
    return False


edges = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"], ["k", "j"]]

def edges_to_adjaency_list(edges):
    graphql= {}
    for edge in edges:
        for i in range(len(edge)):
            graphql[edge[i]] = []
            if i +1 < len(edge):
                graphql[edge[i]].append(edge[i + 1])
            if i -1 >= 0:
                graphql[edge[i]].append(edge[i - 1])
    return graphql

def undirected_graphql_has_path(graph, src, dst, visited:set):
        if src == dst:
            return True
        if src in visited:
            return False
        visited.add(src)
        print(src)
        for neighbor in graph[src]:
            has_path = undirected_graphql_has_path(graph, neighbor, dst, visited)
            if(has_path):
                return True
        return False   


def connected_componets_counts_inslands(graph):
    print(graph)
    visited = set()
    count = 0
    for node in graph:
        if(explore(graph, node, visited)):
            count += 1
    return count
def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    return True
#depth_first_values_iteration(graphq, "a")
#depth_first_values_recursion(graphq, "a")
#breath_first_values_iteration(graphq, "a")
#print(edges_to_adjaency_list(edges))
#undirected_graphql_has_path(edges_to_adjaency_list(edges), "i", "m", set())
# print(connected_componets_counts_inslands({
#     0: [8, 1, 5],
#     1: [0],
#     5: [0, 8],
#     8: [0, 5],
#     2: [3, 4],
#     3: [2, 4],
#     4: [3, 2]
# }))


def largest_component_recursive(graph):
    print(graph)
    largest_size =0
    visited = set()
    for node in graph:
        size = explore_recursive(graph, node, visited, 0)
        if size > largest_size:
            largest_size = size
    return largest_size
def explore_recursive(graph, current, visited:set, size):
    if current in visited:
        return 0
    
    visited.add(current)
    for neighbor in graph[current]:
        size += explore_recursive(graph, neighbor, visited, 1)
    return size

new_edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]

def shortest_path(graph, source, destination,):
    queue = [(source, 0)]
    visited = set([source])
    while len(queue) > 0:
        node, distance = queue.pop(0)
        if node == destination:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    return -1


def island_count(graphq):
    visited = set()
    count = 0
    size = 9999999999999
    for rown, rowv in enumerate(graphq):
        #print("row", rown, rowv )
        for coln, colv in enumerate(rowv):
            #print("col", coln, colv)
            if graphq[rown][coln] == "L" and (rown, coln) not in visited:
                new_size = explore_island(graphq, (rown, coln), visited, 1)
                size =  min(size, new_size)
                count += 1
            else:
                visited.add((rown, coln))
    if(size == 9999999999999):
        size = 0
    return count, size

def explore_island(grapqh, node, visited, size):
    if node in visited:
        return 0
    visited.add(node)
    for neighbor in get_neigh(grapqh, node):
        size += explore_island(grapqh, neighbor, visited, 1)
    return size


def get_neigh(graph, node):
    row, col = node
    neighs = []
    if col + 1 < len(graph[row]) and graph[row][col + 1] == "L":
        neighs.append((row, col + 1))
    if col - 1 >= 0 and graph[row][col - 1] == "L":
        neighs.append((row, col - 1))
    if row + 1 < len(graph) and graph[row + 1][col] == "L":
        neighs.append((row + 1, col))
    if row - 1 >= 0 and graph[row - 1][col] == "L":
        neighs.append((row - 1, col))
    return neighs
# print(largest_component_recursive({ 0: [8, 1, 5],
#     1: [0],
#     5: [0, 8],
#     8: [0, 5],
#     2: [3, 4],
#     3: [2, 4],
#     4: [3, 2]
# }))

# print(shortest_path(edges_to_adjaency_list(new_edges), "w", "z", ))
# print(edges_to_adjaency_list(new_edges))
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
grid_2 = [
    ['L', 'L', 'L', 'L', 'L'],
    ['L', 'L', 'L', 'L', 'L'],
    ['L', 'L', 'L', 'L', 'L'],
]
grid_3 = [
    ["W", "W"],
    ["W", "W"],
    ["W", "W"],
]
grid_4 = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

grid_5 = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]
grid_6 = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]
def minimum_island_size(grid):
    pass
print(island_count(grid))
print(island_count(grid_2))
print(island_count(grid_3))
print(island_count(grid_4))
print(island_count(grid_5))
print(island_count(grid_6))
