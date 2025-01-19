import matplotlib.pyplot as plt
import networkx as nx

# Create the graph
G = nx.Graph()

# Define LRT and MRT stations
lrt2_stations = [
    "Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore",
    "Betty Go-Belmonte", "Cubao", "Anonas", "Katipunan", "Santolan", "Antipolo"
]

mrt3_stations = [
    "North Avenue", "Quezon Avenue", "GMA Kamuning", "Araneta Center-Cubao",
    "Santolan-Annapolis", "Ortigas", "Shaw Boulevard", "Boni",
    "Guadalupe", "Buendia", "Ayala", "Magallanes", "Taft Avenue"
]

lrt1_stations = [
    "Roosevelt", "Balintawak", "Monumento", "5th Avenue", "R. Papa",
    "Abad Santos", "Blumentritt", "Tayuman", "Bambang", "Doroteo Jose",
    "Carriedo", "Central Terminal", "United Nations (UN)", "Pedro Gil",
    "Quirino", "Vito Cruz", "Gil Puyat", "Libertad", "EDSA", "Baclaran"
]

# Add edges for LRT 2
for i in range(len(lrt2_stations) - 1):
    G.add_edge(lrt2_stations[i], lrt2_stations[i + 1], color="blue")

# Add edges for MRT 3
for i in range(len(mrt3_stations) - 1):
    G.add_edge(mrt3_stations[i], mrt3_stations[i + 1], color="green")

# Add edges for LRT 1
for i in range(len(lrt1_stations) - 1):
    G.add_edge(lrt1_stations[i], lrt1_stations[i + 1], color="red")

# Add connections between lines
G.add_edge("Cubao", "Araneta Center-Cubao", color="black")  # LRT 2 to MRT 3
G.add_edge("Recto", "Doroteo Jose", color="black")  # LRT 2 to LRT 1
G.add_edge("Taft Avenue", "EDSA", color="black")  # MRT 3 to LRT 1

# Define positions for stations
positions = {
    # LRT2 positions
    "Recto": (1, 5), "Legarda": (2, 5), "Pureza": (3, 5), "V. Mapa": (4, 5),
    "J. Ruiz": (5, 5), "Gilmore": (6, 5), "Betty Go-Belmonte": (7, 5), 
    "Cubao": (8, 5), "Anonas": (9, 5), "Katipunan": (10, 5), "Santolan": (11, 5), "Antipolo": (12,5),
    
    # MRT3 positions
    "North Avenue": (6, 11), "Quezon Avenue": (8.5, 9), "GMA Kamuning": (8.5,7),
    "Araneta Center-Cubao": (8.5, 5), "Santolan-Annapolis": (8.5, 3),
    "Ortigas": (8.5, 1), "Shaw Boulevard": (8, 0), "Boni": (6, -1),
    "Guadalupe": (5, -2), "Buendia": (4, -4), "Ayala": (3, -4),
    "Magallanes": (2, -4), "Taft Avenue": (1, -4),

    # LRT1 positions
    "Roosevelt": (2, 12), "Balintawak": (1, 12), "Monumento": (0, 12),
    "5th Avenue": (0, 11), "R. Papa": (0, 10), "Abad Santos": (0, 9),
    "Blumentritt": (0, 8), "Tayuman": (0, 7), "Bambang": (0, 6),
    "Doroteo Jose": (0, 5), "Carriedo": (0, 4), "Central Terminal": (0, 3),
    "United Nations (UN)": (0, 2), "Pedro Gil": (0, 1), "Quirino": (0, 0),
    "Vito Cruz": (0, -1), "Gil Puyat": (0, -2), "Libertad": (0, -3),
    "EDSA": (0, -4), "Baclaran": (0, -5),
}

# Get edge colors
edges = G.edges(data=True)
colors = [edge[2]["color"] for edge in edges]

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(
    G, pos=positions, with_labels=True, node_size=50, font_size=8,
    edge_color=colors, node_color="lightgray"
)
plt.title("Metro Manila Rail Transit System")
plt.axis("off")
plt.show()

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