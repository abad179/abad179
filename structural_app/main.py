"""Entrada de línea de comandos para el ejemplo de viga."""

from __future__ import annotations

import argparse
import numpy as np

from typing import Any

from beam import SimpleBeam
from plot import plot_results


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Calcula esfuerzos en una viga")
    parser.add_argument("length", type=float, help="Longitud de la viga [m]")
    parser.add_argument("load", type=float, help="Carga distribuida [kN/m]")
    parser.add_argument(
        "--x",
        type=float,
        nargs="*",
        default=[0.0],
        help="Posiciones donde evaluar [m]",
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        help="Muestra una ventana con los diagramas",
    )
    args = parser.parse_args(argv)

    beam = SimpleBeam(args.length, args.load)
    Rx, Ry = beam.reactions()
    print(f"Reacciones: R1 = {Rx:.2f} kN, R2 = {Ry:.2f} kN")
    print(f"Cortante máximo: {beam.max_shear():.2f} kN")
    print(f"Momento máximo: {beam.max_moment():.2f} kN*m")

    x = np.asarray(args.x)
    V = beam.shear_at(x)
    M = beam.moment_at(x)
    for xi, vi, mi in zip(x, V, M):
        print(f"x={xi:.2f} m -> V={vi:.2f} kN, M={mi:.2f} kN*m")

    if args.plot:
        plot_results(beam)


if __name__ == "__main__":
    main()
