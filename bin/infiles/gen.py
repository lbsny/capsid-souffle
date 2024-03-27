import math
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#sns.set_theme()


def generate_capsid():
    coords = []
    trimer_vertices = []
    layer_spacing = 1.0  # needs adjusting!

    # Define the number of beads per layer
    beads_per_layer = [12, 18, 18, 21]  # 69 total beads (frame only)
    num_layers = len(beads_per_layer)

    for layer, num_beads in enumerate(beads_per_layer, start=1):
        z = (num_layers - layer) * layer_spacing

        # Calculate radius for this layer
        layer_radius = np.sqrt(3) * layer / 2

        # Find  angles for equilateral triangles inscribed in a circle
        angles = np.linspace(0, 2*np.pi, 3, endpoint=False)

        # Calculate vertex coords for this layer, also add them to a global vertex list just in case
        layer_vertices = []
        for angle in angles:
            x = layer_radius * np.cos(angle)
            y = layer_radius * np.sin(angle)
            trimer_vertices.append((x, y, z))
            layer_vertices.append((x, y, z))

        # Insert beads along the straight lines connecting vertices
        for i in range(len(layer_vertices)):
            x1, y1, _ = layer_vertices[i]
            x2, y2, _ = layer_vertices[(i + 1) % len(layer_vertices)]  # Connect last vertex to first
            for j in range((num_beads // 3)):  # Distribute beads along each side (doing it this way allows all coords to be in one array, but subtract 1 from the range arg if you want to plot the vertices seperately) 
                print("Placing bead {} of {} on face {} of layer {}" .format(j+1, (num_beads // 3) - 1, i+1, layer))
                # Interpolate coordinates between vertices
                x = x1 + (x2 - x1) * (j + 1) / (num_beads // 3)
                y = y1 + (y2 - y1) * (j + 1) / (num_beads // 3)
                coords.append((x, y, z))

    return np.array(coords), np.array(trimer_vertices)

# Example usage
capsid_coords, vertices = generate_capsid()
coords_copy = capsid_coords.copy()
#capsid_coords = np.round(capsid_coords, 4)
#print(capsid_coords)
#print(vertices)

df = pd.DataFrame(coords_copy, columns=['x', 'y', 'z'])
print(df.to_string())
df.to_csv("luke_trimer", sep=' ', index=True, index_label='index')


fig0 = plt.figure()
ax = plt.axes(projection='3d')
#ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], s=150, alpha=0.75, c='g')
ax.scatter(capsid_coords[:,0], capsid_coords[:,1], capsid_coords[:,2], s=150 ,alpha=0.75)

plt.show()
