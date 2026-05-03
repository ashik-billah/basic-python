import numpy as np
import math

# -----------------------------
# Input Parameters
# -----------------------------
alpha = 45  # angle in degrees
L = 0.5  # projection length

# Convert angle to radians
alpha_rad = math.radians(alpha)

# -----------------------------
# Define a 3D Point
# -----------------------------
point_3d = np.array([2, 3, 4])  # (x, y, z)


# -----------------------------
# Oblique Projection Function
# -----------------------------
def oblique_projection(point, alpha_rad, L):
    x, y, z = point

    x_proj = x + L * z * math.cos(alpha_rad)
    y_proj = y + L * z * math.sin(alpha_rad)

    return np.array([x_proj, y_proj])


# Project single point
projected_point = oblique_projection(point_3d, alpha_rad, L)

print("Original Point:", point_3d)
print("Projected Point:", projected_point)

# -----------------------------
# Define Cube (8 vertices)
# -----------------------------
cube = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# Edges of cube (for visualization)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# -----------------------------
# Project All Cube Points
# -----------------------------
projected_cube = []

for point in cube:
    proj = oblique_projection(point, alpha_rad, L)
    projected_cube.append(proj)

projected_cube = np.array(projected_cube)

print("\nOriginal Cube Matrix:\n", cube)
print("\nProjected Cube Matrix:\n", projected_cube)

# -----------------------------
# Visualization
# -----------------------------
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(121, projection='3d')
for e in edges:
    p1 = cube[e[0]]
    p2 = cube[e[1]]

    ax.plot([p1[0], p2[0]],
            [p1[1], p2[1]],
            [p1[2], p2[2]])

ax.set_title("3D Cube")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax2 = fig.add_subplot(122)
for e in edges:
    p1 = projected_cube[e[0]]
    p2 = projected_cube[e[1]]

    ax2.plot([p1[0], p2[0]],
             [p1[1], p2[1]])

ax2.set_title("Oblique Projection (2D)")
ax2.set_xlabel("X'")
ax2.set_ylabel("Y'")
ax2.axis('equal')

plt.tight_layout()
plt.show()
