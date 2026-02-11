import itertools
import numpy as np
import pyvista as pv


def plot_hypercube(n, path=None):

    vertices = np.array(list(itertools.product([-1, 1], repeat=n)))

    # Projeção nD → 3D
    projected = []

    for v in vertices:
        if n <= 3:
            padded = np.pad(v, (0, 3 - n))
            projected.append(padded[:3])
        else:
            w = np.sum(v[3:])
            factor = 1 / (2 - 0.3 * w)
            projected.append(v[:3] * factor)

    projected = np.array(projected)

    plotter = pv.Plotter()
    plotter.add_axes()

    cloud = pv.PolyData(projected)
    plotter.add_mesh(cloud, point_size=12, render_points_as_spheres=True)

    # Conectar arestas (Hamming = 1)
    for i, v1 in enumerate(vertices):
        for j, v2 in enumerate(vertices):
            if i < j:
                if np.sum(v1 != v2) == 1:
                    line = pv.Line(projected[i], projected[j])
                    plotter.add_mesh(line)

    # Destacar caminho
    if path:
        for i in range(len(path) - 1):
            line = pv.Line(projected[path[i]], projected[path[i+1]])
            plotter.add_mesh(line, color="red", line_width=5)

    plotter.show(auto_close=False)

    plotter.show()
    input("Pressione ENTER para fechar...")

