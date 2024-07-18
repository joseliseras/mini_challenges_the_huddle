
grafo = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A', 'E'},
    'D': {'B'},
    'E': {'C'}
  
}

def dfs(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(nodo)
    print(nodo, end=' ')
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)


dfs(grafo, 'A')
