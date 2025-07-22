import numpy as np

class SimpleBeam:
    """Modelo de viga simplemente apoyada con carga uniformemente distribuida"""
    def __init__(self, length: float, load: float):
        """Inicializa la viga.

        Parameters
        ----------
        length : float
            Longitud de la viga (m).
        load : float
            Carga distribuida (kN/m).
        """
        self.length = length
        self.load = load

    def reactions(self):
        """Calcula las reacciones en los apoyos."""
        R = self.load * self.length / 2
        return R, R

    def max_shear(self):
        """Retorna el cortante máximo absoluto."""
        return self.load * self.length / 2

    def max_moment(self):
        """Retorna el momento flector máximo absoluto."""
        return self.load * self.length**2 / 8
