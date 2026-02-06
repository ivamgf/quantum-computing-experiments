import matplotlib
matplotlib.use("TkAgg")  # Força backend gráfico no Windows

import matplotlib.pyplot as plt


def plot_counts(counts: dict, title: str, filename: str):
    """
    Plota e salva gráfico de distribuição de estados.
    """

    states = list(counts.keys())
    values = list(counts.values())

    plt.figure()
    plt.bar(states, values)
    plt.xlabel("Estados medidos")
    plt.ylabel("Contagem")
    plt.title(title)

    # Salvar imagem
    plt.savefig(filename)

    # Mostrar janela
    plt.show(block=True)

    plt.close()
