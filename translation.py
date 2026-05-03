import matplotlib.pyplot as plt

# -----------------------------
# Original Point
# -----------------------------
P = [2, 3, 1]   # (x, y, 1)

# Translation values
tx, ty = 4, 2

# -----------------------------
# Translation Matrix (Homogeneous)
# -----------------------------
T = [
    [1, 0, tx],
    [0, 1, ty],
    [0, 0, 1]
]

# -----------------------------
# Manual Matrix Multiplication
# -----------------------------
P_new = [0, 0, 0]

for i in range(3):
    for j in range(3):
        P_new[i] += T[i][j] * P[j]

# Extract new point
x_new = P_new[0]
y_new = P_new[1]

print("Original Point:", (P[0], P[1]))
print("Translated Point:", (x_new, y_new))

# -----------------------------
# Plotting
# -----------------------------
plt.figure(figsize=(6,6))

# Original point
plt.scatter(P[0], P[1])
plt.text(P[0]+0.2, P[1]+0.2, f"Original: ({P[0]}, {P[1]})")

# Translated point
plt.scatter(x_new, y_new)
plt.text(x_new+0.2, y_new+0.2, f"Translated: ({x_new}, {y_new})")

# Arrow showing movement
plt.arrow(P[0], P[1], tx, ty, head_width=0.3, length_includes_head=True)

plt.xlim(0, 10)
plt.ylim(0, 10)

plt.axhline(0)
plt.axvline(0)

plt.grid()
plt.title("Translation using Homogeneous Matrix")

plt.show()
