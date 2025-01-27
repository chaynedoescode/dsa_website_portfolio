import networkx as nx
import plotly.graph_objects as go

# Define the graph
G = nx.Graph()

# Define LRT and MRT stations
lrt2_stations = ["Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore",
                 "Betty Go-Belmonte", "Cubao", "Anonas", "Katipunan", "Santolan", "Antipolo"]
mrt3_stations = ["North Avenue", "Quezon Avenue", "GMA Kamuning", "Araneta Center-Cubao",
                 "Santolan-Annapolis", "Ortigas", "Shaw Boulevard", "Boni",
                 "Guadalupe", "Buendia", "Ayala", "Magallanes", "Taft Avenue"]
lrt1_stations = ["Roosevelt", "Balintawak", "Monumento", "5th Avenue", "R. Papa",
                 "Abad Santos", "Blumentritt", "Tayuman", "Bambang", "Doroteo Jose",
                 "Carriedo", "Central Terminal", "United Nations (UN)", "Pedro Gil",
                 "Quirino", "Vito Cruz", "Gil Puyat", "Libertad", "EDSA", "Baclaran"]

# Add edges (similar to your original code)
for i in range(len(lrt2_stations) - 1):
    G.add_edge(lrt2_stations[i], lrt2_stations[i + 1], color="blue")
for i in range(len(mrt3_stations) - 1):
    G.add_edge(mrt3_stations[i], mrt3_stations[i + 1], color="green")
for i in range(len(lrt1_stations) - 1):
    G.add_edge(lrt1_stations[i], lrt1_stations[i + 1], color="red")

# Add connections
G.add_edge("Cubao", "Araneta Center-Cubao", color="black")
G.add_edge("Recto", "Doroteo Jose", color="black")
G.add_edge("Taft Avenue", "EDSA", color="black")

# Positions
positions = {
    # LRT2 positions
    "Recto": (1, 5), "Legarda": (2, 5), "Pureza": (3, 5), "V. Mapa": (4, 5),
    "J. Ruiz": (5, 5), "Gilmore": (6, 5), "Betty Go-Belmonte": (7, 5),
    "Cubao": (8, 5), "Anonas": (9, 5), "Katipunan": (10, 5), "Santolan": (11, 5), "Antipolo": (12, 5),

    # MRT3 positions
    "North Avenue": (6, 11), "Quezon Avenue": (8.5, 9), "GMA Kamuning": (8.5, 7),
    "Araneta Center-Cubao": (8.5, 5.5), "Santolan-Annapolis": (8.5, 3),
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

# Ensure positions is a dictionary
if not isinstance(positions, dict):
    raise TypeError("positions should be a dictionary")

# Create edge traces for Plotly
edge_traces = []
for edge in G.edges(data=True):
    x0, y0 = positions[edge[0]]
    x1, y1 = positions[edge[1]]
    color = edge[2]["color"]

    # Check if the edge is an interchange (color = black)
    if color == "black":
        edge_traces.append(
            go.Scatter(
                x=[x0, x1], y=[y0, y1],
                line=dict(width=2, color=color, dash="dash"),  # Dashed black line
                hoverinfo="none",
                mode="lines",
                showlegend=False  # Do not show legend for individual edges
            )
        )
    else:
        edge_traces.append(
            go.Scatter(
                x=[x0, x1], y=[y0, y1],
                line=dict(width=2, color=color),
                hoverinfo="none",
                mode="lines",
                showlegend=False  # Do not show legend for individual edges
            )
        )

# Add dummy traces for the legend
legend_traces = [
    go.Scatter(
        x=[None], y=[None],
        mode="lines",
        line=dict(width=2, color="blue"),
        hoverinfo="none",
        name="LRT 2"
    ),
    go.Scatter(
        x=[None], y=[None],
        mode="lines",
        line=dict(width=2, color="green"),
        hoverinfo="none",
        name="MRT 3"
    ),
    go.Scatter(
        x=[None], y=[None],
        mode="lines",
        line=dict(width=2, color="red"),
        hoverinfo="none",
        name="LRT 1"
    ),
    go.Scatter(
        x=[None], y=[None],
        mode="lines",
        line=dict(width=2, color="black", dash="dash"),
        hoverinfo="none",
        name="Interchange"
    ),
    go.Scatter(
        x=[None], y=[None],
        mode="markers",
        marker=dict(size=10, color="lightgray"),
        hoverinfo="none",
        name="Stations"
    )
]

# Create node trace
node_trace = go.Scatter(
    x=[positions[node][0] for node in G.nodes()],
    y=[positions[node][1] for node in G.nodes()],
    mode="markers+text",
    text=list(G.nodes()),
    textposition="top left",
    marker=dict(size=10, color="lightgray"),
    name="Stations",
    showlegend=False  # Do not show legend for individual nodes
)

# Create the figure
fig = go.Figure(data=edge_traces + [node_trace] + legend_traces)
fig.update_layout(
    showlegend=True,
    legend=dict(
        x=1,
        y=1,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=2
    ),
    xaxis=dict(showgrid=False, zeroline=False),
    yaxis=dict(showgrid=False, zeroline=False),
    plot_bgcolor="#f0f0f0",  # Light grey background
)

# Save to HTML
fig.write_html("rail_map_with_interchanges.html")