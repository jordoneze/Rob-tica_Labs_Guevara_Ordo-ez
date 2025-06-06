# Laboratorio No. 01 - 2025-I - Robótica de Desarrollo, Intro a ROS 2 Humble - Turtlesim
## Video
Video Explicativo Lab1
'[https://www.youtube-nocookie.com/embed/URL](https://youtu.be/5mlHX-qmWMc)'



## Objetivos.
Para el desarrollo del laboratorio se plantean los siguientes objetivos iniciales:

1. Conocer y explicar los conceptos básicos de ROS (Robot Operating System).
2. Usar los comandos fundamentales de Linux.
3. Conectar nodos de ROS 2 con Python.

 Una vez cumplidos estos objetivos, se desarrollarán dos actividades orientadas a consolidar y aplicar los conocimientos adquiridos. La primera actividad consiste en implementar el control del movimiento de la tortuga del simulador turtlesim a través del teclado. La segunda actividad tiene como finalidad programar el trazado automático de letras personalizadas utilizando dicho simulador.

## Procedimientos realizados.

Se llevó a cabo una investigación preliminar sobre el funcionamiento de los servicios en ROS 2 y su llamado desde scripts en Python. Asimismo, se revisó el código desarrollado durante las sesiones prácticas del laboratorio, con el fin de establecer una base sobre la cual construir las soluciones propuestas. Posteriormente, se exploraron métodos para la lectura de teclas e ingreso de datos desde la terminal, considerando los requisitos de las actividades planteadas. Con esta información, se procedió a implementar el código correspondiente a partir de los diagramas de flujo diseñados, realizando pruebas iterativas para la detección y corrección de errores. 

## Decisiones de diseño.
En la primera actividad, se establece un ángulo de 0.18 radianes y una velocidad de 0.3 , considerando que el tiempo de ejecución es breve. Esta configuración permite que el cambio en el movimiento de la tortuga sea perceptible, pero lo suficientemente sutil como para mantener un desplazamiento controlado. De esta manera, se logra una mayor precisión en la trayectoria, facilitando la generación de formas más definidas durante la simulación.

En la segunda actividad, se opta por limitar el tiempo de ejecución de cada trazo y ajustar las velocidades. Asimismo, se decide realizar el trazado de las letras utilizando únicamente líneas rectas. Esta elección responde al hecho de que no se emplean coordenadas absolutas y el ángulo de orientación puede presentar variaciones (en el orden de milésimas) en cada ejecución. El uso de curvas acentuaría dichas desviaciones, haciendo más notoria la inclinación no deseada en el trazado. 


## Funcionamiento general del proyecto.


Para la actividad asociada a controlar la tortuga del simulador turtlesim con las flechas del teclado se palntea el diagrama de flujo a continuación:

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

Para la actividad que implica el dibujar letras personalizadas, se plantea el siguiente diagrama de flujo, las letras elegidas son "C,E,G,J,M,O,S,X" correspondientes a las iniciales de los nombres y apellidos de los integrantes del grupo. 



```mermaid
---
config:
  theme: redux
---
flowchart TD
    A(["Inicio"]) --> B["Inicializar elementos de ROS2"]
    B --> C["Crear el nodo"]
    C --> D["Llamar servicios"]
    D --> E_1["Solicitar letra de la terminal"]
    E_1 --> N["Leer letra de la terminal"]
    N --> F{"¿La letra ingresada es la C?"}
    F -- Si --> G["Mover la tortuga dibujando la letra C"]
    F -- No --> H{"¿La letra ingresada es la E?"}
    H -- Si --> I["Mover la tortuga dibujando la letra E"]
    H -- No --> J{"¿La letra ingresada es la G?"}
    J -- Si --> K["Mover la tortuga dibujando la letra G"]
    J -- No --> L{"¿La letra ingresada es la J?"}
    L -- Si --> M["Mover la tortuga dibujando la letra J"]
    L -- No --> M_1{"¿La letra ingresada es la M?"}
    M_1 -- Si --> M_2["Mover la tortuga dibujando la letra M"]
    M_1 -- No --> N_1{"¿La letra ingresada es la O?"}
    N_1 -- Si --> O_1["Mover la tortuga dibujando la letra O"]
    N_1 -- No --> P_1{"¿La letra ingresada es la S?"}
    P_1 -- Si --> Q_1["Mover la tortuga dibujando la letra S"]
    P_1 -- No --> R_1{"¿La letra ingresada es la X?"}
    R_1 -- Si --> S_1["Mover la tortuga dibujando la letra X"]
    R_1 -- No --> T_1["Mostrar el mensaje "Letra no válida""]

    M --> E["Mover a posición inicial"]
    K --> E
    I --> E
    G --> E
    M_2 --> E
    O_1 --> E
    Q_1 --> E
    S_1 --> E
    T_1 --> E
    E --> D_2["Limpiar trayectoria anterior"]
    D_2 --> E_1

```
Los resultados obtenidos son: 

![WhatsApp Image 2025-04-27 at 10 35 55 PM](https://github.com/user-attachments/assets/623fcd76-a081-4df0-bccf-f96c7115ce20)

![WhatsApp Image 2025-04-27 at 10 35 55 PM (1)](https://github.com/user-attachments/assets/0f92600b-0441-4491-94fc-a937bb58b20e)

![WhatsApp Image 2025-04-27 at 10 35 55 PM (2)](https://github.com/user-attachments/assets/7cc86b9e-648a-44e4-b8c4-fabe5c7732cf)

![WhatsApp Image 2025-04-27 at 10 35 55 PM (3)](https://github.com/user-attachments/assets/5dc3a38a-8500-42d1-be3e-939c8d166042)

![WhatsApp Image 2025-04-27 at 10 35 55 PM (4)](https://github.com/user-attachments/assets/1b3eb131-9d30-43fd-a8ec-dff042dd6534)

![WhatsApp Image 2025-04-27 at 10 35 56 PM](https://github.com/user-attachments/assets/4f5058a9-8d8f-4aee-9d64-8545966f03e6)

![WhatsApp Image 2025-04-27 at 10 35 56 PM (1)](https://github.com/user-attachments/assets/7a46547f-69b8-4785-b1c0-7b4d0f20782a)

![WhatsApp Image 2025-04-27 at 10 35 56 PM (2)](https://github.com/user-attachments/assets/00d381b3-2a00-4d47-b2f6-0903065c460f)


Para la ejecución del código, se debe tener el archivo de Python en la ubicación correspondiente en el proyecto y ejecutar las siguientes lineas de código en la terminal:
```
source /opt/ros/humble/setup.bash
ros2 run turtlesim turtlesim_node
```
En otra terminal se debe ejecutar, para la actividad 1: 
```
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
ros2 run my_turtle_controller move_turtle
```
Para la actividad 2:
```
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
ros2 run my_turtle_controller my_scripy2
```




