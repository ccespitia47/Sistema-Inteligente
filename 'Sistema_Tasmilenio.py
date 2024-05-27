'Sistema_Tasmilenio.py'
import networkx as nx

# Definimos una heurística simple
def heuristica(nodo_actual, nodo_objetivo):
    # Heurística simple basada en la distancia Manhattan
    # Como ejemplo simple, usaremos una heurística fija, en un caso real esto debería ser calculado según el mapa.
    return 1

# Definimos la función principal para encontrar la mejor ruta usando A*
def mejor_ruta():
    # Creamos un grafo dirigido
    G = nx.DiGraph()

    # Añadimos nodos y aristas (representando estaciones y conexiones)
    estaciones = [
        ("Suba Calle 100", "Movistar Arena", 5),
        ("Movistar Arena", "U.Nacional", 2),
        ("U.Nacional", "Ricaurte", 4),
        ("Ricaurte", "Comuneros", 3),
        ("Comuneros", "Perdomo", 6),
        ("Suba Calle 100", "U.Nacional", 8),
        ("U.Nacional", "Comuneros", 5),
        ("Movistar Arena", "Ricaurte", 3),
        ("Ricaurte", "Perdomo", 7)
    ]

    # Añadimos las aristas al grafo
    for origen, destino, peso in estaciones:
        G.add_edge(origen, destino, weight=peso)

    # Usamos el algoritmo A* para encontrar la mejor ruta
    ruta_optima = nx.astar_path(G, source="Suba Calle 100", target="Perdomo", heuristic=heuristica)
    distancia_total = nx.astar_path_length(G, source="Suba Calle 100", target="Perdomo", heuristic=heuristica)

    # Imprimimos la ruta óptima y la distancia total
    print("La mejor ruta desde Suba Calle 100 hasta Perdomo es (usando A*):")
    print(" -> ".join(ruta_optima))
    print(f"Distancia total: {distancia_total} unidades")

# Llamamos a la función principal
if __name__ == "__main__":
    mejor_ruta()
