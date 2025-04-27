# Laboratorio No. 01 - 2025-I - Robótica de Desarrollo, Intro a ROS 2 Humble - Turtlesim
## Objetivos.

## Procedimientos realizados.

## Decisiones de diseño.

## Funcionamiento general del proyecto.




```mermaid
---
config:
  theme: redux
---
flowchart TD
    A(["Inicio"]) --> B["Inicializar elementos de ROS2"]
    B --> C["Crear el nodo"]
    C --> D["Llamar servicios"]
    D --> E["Leer tecla de la Terminal"]
    E --> F{"¿La tecla presionada es la flecha hacia arriba?"}
    F -- Si --> G["Mover hacia adelante"]
    F -- No --> H{"¿La tecla presionada es la flecha hacia abajo?"}
    H -- Si --> I["Mover hacia atras"]
    H -- No --> J{"¿La tecla presionada es la flecha izquierda?"}
    J -- Si --> K["Girar a la izquierda"]
    J -- No --> L{"¿La tecla presionada es la flecha derecha?"}
    L -- Si --> M["Girar a la derecha"]
    M --> E
    K --> E
    I --> E
    G --> E

```
