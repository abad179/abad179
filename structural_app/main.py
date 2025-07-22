from beam import SimpleBeam


def main():
    # Ejemplo de uso
    length = 5.0  # m
    load = 10.0   # kN/m
    beam = SimpleBeam(length, load)
    Rx, Ry = beam.reactions()
    print(f"Reacciones: R1 = {Rx:.2f} kN, R2 = {Ry:.2f} kN")
    print(f"Cortante máximo: {beam.max_shear():.2f} kN")
    print(f"Momento máximo: {beam.max_moment():.2f} kN*m")


if __name__ == "__main__":
    main()
