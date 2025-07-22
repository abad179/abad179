# Aplicación Simple de Cálculo Estructural

Esta carpeta contiene un ejemplo básico de una app en Python para
calcular las reacciones, cortantes y momentos de una viga simplemente
apoyada con carga uniformemente distribuida.

## Requisitos

- Python 3.8+
- `numpy`
- `matplotlib` para la visualización opcional

## Ejecución

```bash
python main.py 5 10 --x 0 2.5 5 --plot
```

El programa imprime en consola las reacciones y, si se utiliza la opción
`--plot`, abre una ventana con los diagramas de cortante y momento.

## Uso como módulo

Puedes importar la clase `SimpleBeam` en tu propio código:

```python
from structural_app import SimpleBeam, plot_results

beam = SimpleBeam(5.0, 10.0)
print(beam.reactions())
print(beam.moment_at(2.5))
plot_results(beam)
```
