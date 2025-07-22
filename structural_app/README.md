# Aplicación Simple de Cálculo Estructural

Esta carpeta contiene un ejemplo básico de una app en Python para
calcular las reacciones, cortantes y momentos de una viga simplemente
apoyada con carga uniformemente distribuida.

## Requisitos

- Python 3.8+
- `numpy`

## Ejecución

```bash
python main.py 5 10 --x 0 2.5 5
```

El programa imprime en consola las reacciones y los valores de cortante y
momento en las posiciones indicadas.

## Uso como módulo

Puedes importar la clase `SimpleBeam` en tu propio código:

```python
from beam import SimpleBeam

beam = SimpleBeam(5.0, 10.0)
print(beam.reactions())
print(beam.moment_at(2.5))
```
