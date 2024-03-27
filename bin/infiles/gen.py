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
    layer_spacing = 1.0  # Adjust as needed

    # Define the number of beads per layer
    beads_per_layer = [12, 18, 18, 21]  # Total: 69 beads
    num_layers = len(beads_per_layer)

    for layer, num_beads in enumerate(beads_per_layer, start=1):
        z = (num_layers - layer) * layer_spacing

        # Calculate the radius for this layer
        layer_radius = np.sqrt(3) * layer / 2

        # Calculate the angles for equilateral triangles inscribed in a circle
        angles = np.linspace(0, 2*np.pi, 3, endpoint=False)

        # Calculate the vertices of the triangular frame for this layer
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
            for j in range((num_beads // 3)):  # Distribute beads equally along each side (doing it this way allows all coords to be in one array, but subtract 1 from the range arg if you want to plot the vertices seperately) 
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

exit()


# def generate_hollow_pyramid_coordinates(num_layers):
#     coordinates = []

#     for layer in range(num_layers):
#         radius = layer + 1
#         theta = 0

#         for edge in range(3):  # Assuming a pyramid with 6 sides
#             x = radius * math.cos(theta)
#             y = radius * math.sin(theta)
#             z = num_layers-(layer+1)
#             coordinates.append((x, y, z, layer))

#             theta += (2 * math.pi) / 3  # Angle between particles
#             print(theta)

#     coordinates.insert(0, (0,0, num_layers, -1))

#     return np.round(np.array(coordinates), 3)


# def generate_filled_pyramid_coordinates(num_layers):
#     coordinates = []

#     for layer in range(num_layers):
#         radius =  layer + 1
#         theta = 0

#         for edge in range(4):  # Assuming a pyramid with 4 sides
#             x_center = radius * math.cos(theta)
#             y_center = radius * math.sin(theta)
#             z_center = num_layers - layer
#             print(x_center, y_center, z_center)

#             # Generate points within the face
#             for i in range(3):  # Number of points within each face
#                 angle = (2 * math.pi / 3) * i
#                 print("Angle", angle)
#                 x = x_center + 0.5 * math.cos(angle)  # Adjust the factor for distribution within the face
#                 y = y_center + 0.5 * math.sin(angle)  # Adjust the factor for distribution within the face
#                 z = z_center
#                 coordinates.append((x, y, z))

#             theta += (2 * math.pi) / 4  # Angle between particles
#             print(theta)

#     return np.array(coordinates)


# def points_on_triangle(v, n):
#     """
#     Give n random points uniformly on a triangle.

#     The vertices of the triangle are given by the shape
#     (2, 3) array *v*: one vertex per row.
#     """
#     x = np.sort(np.random.rand(2, n), axis=0)
#     return np.column_stack([x[0], x[1]-x[0], 1.0-x[1]]) @ v


# # Example usage with 5 particles
# num_layers = 4
# edge_coordinates = generate_hollow_pyramid_coordinates(num_layers)
# print("Here are the edge coordinates:")
# print(edge_coordinates)

# bvertices = edge_coordinates[-3:, :2]
# print(bvertices)
# points = points_on_triangle(bvertices, 1000)
# basex, basey = zip(*points)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.scatter3D(edge_coordinates[:,0], edge_coordinates[:,1], edge_coordinates[:,2])
# ax.scatter(basex,basey)
# plt.show()

# df = pd.DataFrame(edge_coordinates, columns=["x", "y", "z", "layer"])
# print(df)

#Plotting the original trimer as a reference

# trimer = pd.read_csv("trimer_MVM", skiprows=6, sep='\s+', nrows=78)
# print(trimer.to_string())


# fig2 = plt.figure()
# ax2 = plt.axes(projection='3d')
# ax2.scatter(trimer['x'], trimer['y'], trimer['z'], s=200, alpha=0.6)
# plt.show()