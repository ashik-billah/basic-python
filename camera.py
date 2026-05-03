import numpy as np
import matplotlib.pyplot as plt

vertices = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 0],
    [1, 0, 0],
    [0, 0, 1],
    [0, 1, 1],
    [1, 1, 1],
    [1, 0, 1]

])

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

fx, fy = 800, 800
cx, cy = 320, 240
K = np.array([
    [fx, 0, cx],
    [0, fy, cy],
    [0, 0, 1]
])
C = np.array([0, 0, -5])
theta = np.radians(45)
R = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])


# vertices = vertices + np.array([0,0,5])

# projection function
def project_func(points, R, C, K):
    projected = []
    for P in points:
        Pc = R @ (P - C)
        X, Y, Z = Pc
        if Z <= 0:
            projected.append([np.nan, np.nan])
            continue
        # normalize
        x = X / Z
        y = Y / Z

        u = fx * x + cx
        v = fy * y + cy

        projected.append([u, v])
    return np.array(projected)


projected_points = project_func(vertices, R, C, K)
print(projected_points)

# visualize
fig = plt.figure(figsize=(8, 6))

# 2D projection

ax1 = fig.add_subplot(1, 2, 1, )
for edge in edges:
    p1 = projected_points[edge[0]]
    p2 = projected_points[edge[1]]
    ax1.plot([p1[0], p2[0]], [p1[1], p2[1]])
ax1.set_title("2D Projection")
ax1.invert_yaxis()
ax1.grid()

# 3D visualization
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
for edge in edges:
    p1 = vertices[edge[0]]
    p2 = vertices[edge[1]]

    ax2.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]])
ax2.scatter(C[0], C[1], C[2], color='red', label='Camera')
ax2.text(C[0], C[1], C[2], 'Camera')
ax2.set_title("3D Visualization")
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.set_zlabel('Z-axis')
ax2.grid()
plt.show()
