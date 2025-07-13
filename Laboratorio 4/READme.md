# Laboratorio No. 4 - Cinemática Directa - Phantom X - ROS
## Objetivos
- Crear todos los Joint Controllers con ROS para manipular servomotores Dynamixel AX-12 del robot Phantom X Pincher.
- Manipular los tópicos de estado y comando para todos los Joint Controllers del robot Phantom X Pincher.
- Manipular los servicios para todos los Joint Controllers del robot Phantom X Pincher.
- Conectar el robot Phantom X Pincher con Python usando ROS 2.
## Cinemática Directa
![DH](https://github.com/user-attachments/assets/3f850587-a265-42ad-8ed5-8da054932eba)

Con base en los sistemas coordenados planteados en la imagen anterior, se obtiene la tabla de parámetros del robot Phantom X:

| Link  | θ<sub>i</sub> | d<sub>i</sub> | a<sub>i</sub> |  α<sub>i</sub>  |  Offset  |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 1  | θ<sub>1</sub>  | L<sub>1</sub> | 0 | -π/2 | 0 |
|  2|  θ<sub>2</sub> | 0 | L<sub>2</sub> | 0 | -π/2 |
|  3|  θ<sub>3</sub> | 0 | <sub>3</sub> | 0 | π/2 |
|  4|  θ<sub>4</sub> | 0 | <sub>4</sub> | 0 | π/2 |

### Longitudes

Las longitudes referidas en la cinemática directa son:
| Longitud  | [m] |
| ------------- | ------------- |
| L<sub>1</sub>  |   |
| L<sub>2</sub>  |   |
| L<sub>3</sub>  |   |
| L<sub>4</sub>  |   |

### Diagrama del robot con software

## Implementación
### Descripción de Solución Planteada
### Plano de planta (Fisica)
### Funciones utilizadas
### Diagrama de Flujo
```mermaid
---
config:
  theme: 'forest'
  layout: dagre
---
flowchart TD

    L4A(["Inicio"])--> L4B_1["Ir a Home"]
    L4B_1 --> L4B2{"¿La posición selecionada es la número 1?"}
    L4B2 -- Si --> L4B3["Ir a posición 1"]
    L4B2 -- No --> L4B4{"¿La posición selecionada es la número 2?"}
    L4B4 -- Si --> L4B5["Ir a posición 2"]
    L4B4 -- No --> L4B6{"¿La posición selecionada es la número 3?"}
    L4B6 -- Si --> L4B7["Ir a posición 3"]
    L4B6 -- No --> L4B8{"¿La posición selecionada es la número 4?"}
    L4B8 -- Si --> L4B9["Ir a posición 4"]
    L4B8 -- No --> L4B10{"¿La posición selecionada es la número 5?"}
    L4B10 -- Si --> L4B11["Ir a posición 5"]
    L4B11 -- No --> L4B2
    L4B10 -- No --> L4B2
    L4B9 -- No --> L4B2
    L4B7 -- No --> L4B2
    L4B5 -- No --> L4B2 
    L4B3 -- No --> L4B2
```

### Evidencias fotograficas

### Interfaz


## Video 
