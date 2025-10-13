import search

# Definición del problema
ab = search.GPSProblem('A', 'B', search.romania)

# Búsqueda en anchura
result, gen, vis = search.breadth_first_graph_search(ab)
print("\n--- Anchura ---")
print("Ruta:", [n.state for n in result.path()][::-1])
print("Coste total:", result.path_cost)
print("Nodos generados:", gen)
print("Nodos visitados:", vis)

# Búsqueda en profundidad
result, gen, vis = search.depth_first_graph_search(ab)
print("\n--- Profundidad ---")
print("Ruta:", [n.state for n in result.path()][::-1])
print("Coste total:", result.path_cost)
print("Nodos generados:", gen)
print("Nodos visitados:", vis)

# Ramificación y Acotación
result, gen, vis = search.branch_and_bound(ab)
print("\n--- Ramificación y Acotación ---")
print("Ruta:", [n.state for n in result.path()][::-1])
print("Coste total:", result.path_cost)
print("Nodos generados:", gen)
print("Nodos visitados:", vis)

# Ramificación y Acotación con Subestimación
result, gen, vis = search.branch_and_bound_subestimation(ab)
print("\n--- Ramificación y Acotación con Subestimación ---")
print("Ruta:", [n.state for n in result.path()][::-1])
print("Coste total:", result.path_cost)
print("Nodos generados:", gen)
print("Nodos visitados:", vis)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450



import time

# Definir estrategias
strategies = {
    "Anchura": lambda: search.breadth_first_graph_search(ab),
    "Profundidad": lambda: search.depth_first_graph_search(ab),
    "Ramificación y Acotación": lambda: search.branch_and_bound(ab),
    "Ramificación + Subestimación": lambda: search.branch_and_bound_subestimation(ab)
}

results = []

# Ejecutar todas las estrategias
for name, func in strategies.items():
    start = time.time()
    result, gen, vis = func()
    elapsed = time.time() - start
    path = [n.state for n in result.path()][::-1]
    cost = result.path_cost
    results.append([name, " → ".join(path), cost, gen, vis, round(elapsed, 4)])

# Imprimir tabla
print("\n=== COMPARATIVA DE ESTRATEGIAS ===")
header = ["Estrategia", "Ruta", "Coste", "Generados", "Visitados", "Tiempo (s)"]
print(f"{header[0]:<30} | {header[1]:<25} | {header[2]:<6} | {header[3]:<9} | {header[4]:<9} | {header[5]:<9}")
print("-" * 95)

for row in results:
    print(f"{row[0]:<30} | {row[1]:<25} | {row[2]:<6} | {row[3]:<9} | {row[4]:<9} | {row[5]:<9}")
