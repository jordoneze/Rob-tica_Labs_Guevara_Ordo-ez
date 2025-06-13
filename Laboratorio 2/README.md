# Laboratorio No. 02 - Robótica Industrial - Trayectorias, Entradas y Salidas Digitales.
## Descripción de la solución planteada 


## Diseño del porta-herramienta

![1749647546794](https://github.com/user-attachments/assets/ac25fa75-bf9e-4fcd-a9b7-64cfb0829d0e)
![image](https://github.com/user-attachments/assets/bead3722-0dbd-4252-bd8b-7a7b5afd53ac)
El porta herramienta se diseño con un angulo de 40º para evitar una singularidad. Además se creo considarando las medidas de un marcador borrable EXPO y un resorte encontrado en casa, de una pulgada de longitud con diametro de media pulgada, que tiene el proposito de amortiguar. 

## Trayectorias
![image](https://github.com/user-attachments/assets/a5171156-715e-4516-a474-a220a7d74a7b)

## Diagrama de Flujo
```mermaid
---
config:
  theme: redux
  layout: dagre
---
flowchart TD
    A(["Inicio"]) --> B_1["Se dirige a Home"]
    B_1 --> B{"¿La entrada digital 1 esta encedida?"}
    B -- No --> D{"¿La entrada digital 2 esta encedida?"}
    B -- Si --> E["Enciende Salida Digital 1 (Luz)"]
    E --> F["Se dirige a Home"]
    F  --> G["Realiza la trayectoria del primer nombre"]
    G  --> H["Realiza la trayectoria de la decoración"]
    H  --> I["Realiza la trayectoria del segundo nombre"]
    I --> J["Se dirige a Home"]
    J --> K["Se enciende la banda transportadora"]
    K --> L["Espera cinco segundos"]
    L --> M["Se apaga la banda transportadora"]

    D -- No -->B
    D -- Si --> N["Apaga Salida Digital 1 (Luz)"]
    N --> Ñ["Gira hacia el lateral izquierdo (en posición para cambiar la herramienta)"]
    Ñ-->B
    M-->B
```

## Plano de Planta
![image](https://github.com/user-attachments/assets/be4a7893-433b-4412-91ec-19f462e90c73)

La caja se encuentra ubicada en X=675 mm; Y=110 mm y Z=195 mm con la base del robot como referencia.
La altura de la banda corresponde a Z=195 mm y la longitud es de 400 mm.

## Funciones utilizadas
* MoveJ:
  Desplazamiento del extremo del robot hasta el punto indicado sin garantizar la trayectoria seguida.
  Se utilizo principalmente para llevar el robot desde su ultima posición a la posición de Home.
  
* MoveL:
  Desplazamiento del extremo del robot hasta el punto indicado siguiendo una línea recta.
  Se utilizo para mover el robot en los puntos pertenecientes a las trayectorias de los nombres y la decoración.

## Video con Simulaciones y Práctica Real
