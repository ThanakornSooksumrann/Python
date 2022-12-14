# -*- coding: utf-8 -*-
"""Graph_Node.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U7H_Rzb-KJC_uflTB6jczkGA24ihaqF4
"""

graph = {
  '0' : ['1'],
  '1' : ['0','2'],
  '2' : ['1','3'],
  '3' : ['2','1'],
  '4' : ['3'],
  '5' : [],
  '6' : ['7','8'],
  '7' : ['6','8'],
  '8' : ['6','7'],
}
for i in graph:
  print(i, end = " ")

graph = {
'0' : ['1'],
'1' : ['0','2'],
'2' : ['1','3'],
'3' : ['2','1'],
'4' : ['3'],
'5' : [],
'6' : ['7','8'],
'7' : ['6','8'],
'8' : ['6','7'],
}
visited = [] # List to keep track of visited nodes.
queue = [] #Initialize a queue
node = '';
nodef = '';
def bfs(visited, graph, node, nodef): 
  visited.append(node)
  queue.append(node)

  while queue: 
    s = queue.pop(0)
    print (s, end = " ")
    if s == nodef:
      break
    
    for neighbour in graph[s]: 
        if neighbour not in visited: 
          visited.append(neighbour)
          queue.append(neighbour)

node = input ("Input initial Node : ")
nodef = input ("Input final Node : ")
bfs(visited, graph, node, nodef)

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'B')