import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Tworzenie losowego grafu Watts-Strogatz
n = 10  # Liczba węzłów (agentów)
k = 4   # Średni stopień węzłów 
p = 0.3 # Prawdopodobieństwo przewinięcia krawędzi

graph = nx.watts_strogatz_graph(n, k, p, seed=None)

# Inicjalizacja agenta na losowym węźle
agent_position = random.choice(list(graph.nodes()))

# Funkcja generująca kolejne klatki animacji
def update(frame):
    global agent_position
    
    # Losowe wybranie jednego sąsiada aktualnej pozycji agenta
    neighbors = list(graph.neighbors(agent_position))
    agent_position = random.choice(neighbors)

    # Rysowanie grafu z aktualną pozycją agenta
    plt.clf()
    nx.draw(graph, pos=nx.circular_layout(graph), node_color='lightblue', with_labels=True)
    fig=nx.draw_networkx_nodes(graph, pos=nx.circular_layout(graph), nodelist=[agent_position], node_color='red')
    plt.savefig(("C:\\Users\\dbjd2\\Desktop\\PYTON\\SPACER\\"+f"spacer{frame+1}.jpg"), format="jpg")
    
# Tworzenie animacji
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=10, interval=500)

# Zapisywanie animacji do pliku GIF
ani.save("C:\\Users\\dbjd2\\Desktop\\PYTON\\SPACER\\random_walk.gif", writer='pillow', dpi=300)


# Wyświetlanie animacji
#plt.show()
#plt.close()