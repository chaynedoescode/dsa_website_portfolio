import networkx as nx

# Create a graph
G = nx.Graph()

# Add LRT Line 2 stations
lrt2_stations = [
    "Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore",
    "Betty Go-Belmonte", "Cubao", "Anonas", "Katipunan", "Santolan"
]

# Add MRT Line 3 stations
mrt3_stations = [
    "North Avenue", "Quezon Avenue", "GMA Kamuning", "Araneta Center-Cubao",
    "Santolan-Annapolis", "Ortigas", "Shaw Boulevard", "Boni",
    "Guadalupe", "Buendia", "Ayala", "Magallanes", "Taft Avenue"
]

# Add LRT Line 1 stations
lrt1_stations = [
    "Roosevelt", "Balintawak", "Monumento", "5th Avenue", "R. Papa",
    "Abad Santos", "Blumentritt", "Tayuman", "Bambang", "Doroteo Jose",
    "Carriedo", "Central Terminal", "United Nations (UN)", "Pedro Gil",
    "Quirino", "Vito Cruz", "Gil Puyat", "Libertad", "EDSA", "Baclaran"
]

# Add edges for LRT Line 2
for i in range(len(lrt2_stations) - 1):
    G.add_edge(lrt2_stations[i], lrt2_stations[i + 1])

# Add edges for MRT Line 3
for i in range(len(mrt3_stations) - 1):
    G.add_edge(mrt3_stations[i], mrt3_stations[i + 1])

# Add edges for LRT Line 1
for i in range(len(lrt1_stations) - 1):
    G.add_edge(lrt1_stations[i], lrt1_stations[i + 1])

# Add connections between lines
G.add_edge("Cubao", "Araneta Center-Cubao")  # LRT 2 to MRT 3
G.add_edge("Recto", "Doroteo Jose")  # LRT 2 to LRT 1
G.add_edge("Taft Avenue", "EDSA")  # MRT 3 to LRT 1

def find_shortest_path(graph, source, destination):
    try:
        # Compute the shortest path
        path = nx.shortest_path(graph, source=source, target=destination)
        return path
    except nx.NetworkXNoPath:
        return None

# Accept source and destination station names as inputs
source = input("Enter the source station: ")
destination = input("Enter the destination station: ")

# Find the shortest path
path = find_shortest_path(G, source, destination)

if path:
    print("Shortest path:", " -> ".join(path))
else:
    print("No path found between the given stations.")