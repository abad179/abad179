# Memoria de Cálculo

Este documento describe las ecuaciones utilizadas en la app de ejemplo
para analizar una viga simplemente apoyada con carga distribuida
uniformemente.

## Hipótesis y simplificaciones

- Se considera una viga prismatic que se comporta de manera lineal.
- La carga distribuida actúa a lo largo de toda la luz.
- No se incluyen deformaciones axiales ni otros efectos secundarios.

## Ecuaciones empleadas

1. **Reacciones en los apoyos**

   Para una viga simplemente apoyada con carga uniformemente
   distribuida `q` (en kN/m) y longitud `L`, las reacciones en los
   apoyos son iguales y valen:

   \[ R_1 = R_2 = \frac{qL}{2} \]

2. **Cortante máximo**

   El cortante máximo absoluto coincide con la reacción:

   \[ V_{\text{max}} = \frac{qL}{2} \]

3. **Momento flector máximo**

   El momento máximo se produce en el centro de la viga y está dado por:

   \[ M_{\text{max}} = \frac{qL^2}{8} \]

4. **Distribución de cortante y momento**

   A una distancia `x` desde el extremo izquierdo, los valores son:

   \[ V(x) = q\left(\frac{L}{2} - x\right) \]

   \[ M(x) = \frac{q x (L - x)}{2} \]

Estos resultados son los que devuelve la clase `SimpleBeam` implementada en
`beam.py`. La función `plot_results` permite visualizar gráficamente estos
diagramas a lo largo de la luz.
