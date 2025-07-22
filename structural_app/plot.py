import matplotlib.pyplot as plt
from .beam import SimpleBeam


def plot_results(beam: SimpleBeam, points: int = 50) -> None:
    """Muestra diagramas de cortante y momento para ``beam``.

    Parameters
    ----------
    beam : SimpleBeam
        Instancia de la viga a representar.
    points : int
        Número de puntos para el diagrama.
    """
    x, V, M = beam.diagram(points)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

    ax1.plot(x, V, label="V(x)")
    ax1.set_ylabel("Cortante [kN]")
    ax1.set_xlabel("Posición x [m]")
    ax1.grid(True)

    ax2.plot(x, M, label="M(x)")
    ax2.set_ylabel("Momento [kN*m]")
    ax2.set_xlabel("Posición x [m]")
    ax2.grid(True)

    fig.tight_layout()
    plt.show()

