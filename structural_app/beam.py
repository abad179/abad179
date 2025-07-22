"""Módulo con utilidades para analizar una viga simplemente apoyada.

Se proporcionan funciones para calcular reacciones, cortantes y momentos
en cualquier punto de la luz cuando la viga está sometida a una carga
uniformemente distribuida.
"""

from dataclasses import dataclass
import numpy as np

@dataclass
class SimpleBeam:
    """Modelo de viga simplemente apoyada con carga uniformemente distribuida."""

    length: float
    load: float

    def __post_init__(self) -> None:
        if self.length <= 0:
            raise ValueError("length must be positive")
        if self.load < 0:
            raise ValueError("load cannot be negative")

    # ------------------------------------------------------------------
    #  Resultados básicos
    # ------------------------------------------------------------------

    def reactions(self):
        """Calcula las reacciones en los apoyos."""
        R = self.load * self.length / 2
        return R, R

    def max_shear(self) -> float:
        """Retorna el cortante máximo absoluto."""
        return self.load * self.length / 2

    def max_moment(self) -> float:
        """Retorna el momento flector máximo absoluto."""
        return self.load * self.length**2 / 8

    # ------------------------------------------------------------------
    #  Diagramas internos
    # ------------------------------------------------------------------

    def shear_at(self, x) -> np.ndarray:
        """Cortante en la sección ubicada a una distancia ``x``.

        ``x`` puede ser un escalar o un array de posiciones.
        """
        arr = np.asarray(x, dtype=float)
        if np.any((arr < 0) | (arr > self.length)):
            raise ValueError("x must be within the beam length")
        return self.load * (self.length / 2 - arr)

    def moment_at(self, x) -> np.ndarray:
        """Momento flector en la sección ubicada a una distancia ``x``."""
        arr = np.asarray(x, dtype=float)
        if np.any((arr < 0) | (arr > self.length)):
            raise ValueError("x must be within the beam length")
        return self.load * arr * (self.length - arr) / 2

    def diagram(self, points: int = 50) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Devuelve arrays de posiciones, cortantes y momentos a lo largo de la viga."""
        x = np.linspace(0, self.length, points)
        V = self.shear_at(x)
        M = self.moment_at(x)
        return x, V, M
