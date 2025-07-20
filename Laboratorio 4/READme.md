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
|  3|  θ<sub>3</sub> | 0 | L<sub>3</sub> | 0 | π/2 |
|  4|  θ<sub>4</sub> | 0 | L<sub>4</sub> | 0 | π/2 |
|  5|  θ<sub>5</sub> | L<sub>5</sub> | 0 | 0 | 0 |

### Longitudes

Las longitudes referidas en la cinemática directa son:
| Longitud  | [m] |
| ------------- | ------------- |
| L<sub>1</sub>  | 0.0512  |
| L<sub>2</sub>  |  0.1095 |
| L<sub>3</sub>  |  0.1058 |
| L<sub>4</sub>  |  0.0641 |
| L<sub>5</sub>  |  0.0455 |

### Diagrama del robot con software
Haciendo uso del software Matlab se simula la cinemática directa para hallar un modelo del robot.

<img width="593" height="523" alt="Figure_1" src="https://github.com/user-attachments/assets/f7ed0c0c-0be7-4d69-9442-59412d05c06f" />


## Implementación
### Descripción de Solución Planteada
La solución al laboratorio se desarrolló mediante una combinación de herramientas de software y hardware que permitieron controlar el brazo robótico Phantom X Pincher . Se construyó un sistema  que incluye comunicación con los motores, modelado matemático del robot, y una interfaz gráfica .

Primero, se realizó una medición física del robot para determinar las longitudes de sus eslabones. Con estos datos se definieron los parámetros DH (Denavit-Hartenberg), que describen la estructura del manipulador. Esta información fue usada para modelar el robot en Python utilizando el paquete `roboticstoolbox`, lo cual permitió generar una simulación en 3D de su movimiento y configuraciones.

A nivel de software, se utilizaron dos nodos en ROS 2:

- **Nodo controlador (`pincher_controller`)**: recibe comandos de movimiento y se comunica con los motores Dynamixel mediante la librería `dynamixel_sdk`. Este nodo es el encargado de mover físicamente el brazo robótico hacia la posición seleccionada. Después de moverlo, publica los ángulos reales alcanzados por cada articulación.

- **Nodo de interfaz (`robot_hmi`)**: se encarga de la parte visual e interactiva. Este nodo implementa una interfaz HMI (Human-Machine Interface) creada con PyQt5. En ella, el usuario puede:
  - Ver el logotipo y los nombres de los integrantes del grupo.
  - Seleccionar una de las cinco poses predefinidas.
  - Enviar esa pose al robot con un botón.
  - Ver en pantalla los valores reales de cada articulación en radianes.
  - Visualizar en 3D la configuración actual del robot en tiempo real.

La comunicación entre ambos nodos se realiza por medio de dos tópicos ROS:

- `'move_index'`: envía el número de la pose seleccionada al nodo controlador.
- `'joint_angles'`: envía los valores articulares reales del robot hacia la HMI.

Las cinco poses utilizadas fueron definidas en función de ángulos característicos para verificar el movimiento del brazo. Cada pose fue implementada tanto en la parte física (motores Dynamixel) como en la simulación virtual, y se validó que ambas coincidieran.

Finalmente, se realizó una demostración completa donde se muestra el funcionamiento del sistema: desde la selección de la pose hasta la ejecución física y la visualización gráfica en 3D. Esto permitió comprobar que la cinemática directa fue correctamente implementada y que el sistema completo (modelo, motores, ROS y HMI) funciona de manera integrada.

### Descripción de las funciones utilizadas

En el primer archivo (`control_servo2.py`) se encuentra el código que controla directamente los motores del robot Phantom X. Este programa está hecho para funcionar como un "nodo", es decir, una parte del sistema que se comunica con otras partes por medio de mensajes. La primera función importante es `__init__`, que se encarga de preparar todo lo necesario: se configuran los parámetros como el puerto USB donde está conectado el robot, la velocidad de comunicación y los motores que se van a usar. También se abre la conexión con el robot, y se crean dos canales: uno para enviar los movimientos que se hagan realmente (los ángulos) y otro para recibir qué pose se quiere ejecutar desde la interfaz HMI.

Luego está la función `mover_a_posicion`, que es la que mueve los motores cuando se le da una lista con los valores deseados. Estos valores indican la posición final que se quiere para cada motor. La función primero activa los motores, les dice qué velocidad usar y qué fuerza pueden aplicar. Después les envía el valor objetivo. Una vez hecho eso, espera un momento para que el movimiento termine, convierte las posiciones alcanzadas a radianes (que son las unidades que usamos para los ángulos) y las manda al canal para que la interfaz pueda mostrar lo que el robot realmente hizo.

La función `callback_move_index` es una función que se activa automáticamente cuando llega un mensaje con un número. Ese número representa la pose que se quiere ejecutar. Si el número es `-1`, significa que se quiere apagar los motores. Si es otro número , entonces esa función busca cuál es la pose correspondiente en una lista que ya está guardada y llama a `mover_a_posicion` para ejecutarla. Es decir, esta función recibe las órdenes desde la interfaz y decide qué hacer.

Por último, la función `main` es la que se ejecuta cuando se inicia el script. Se encarga de iniciar todo lo anterior, mantenerlo funcionando mientras se usa el robot, y al final cerrar bien la conexión cuando ya no se necesita.

---

Ahora, en el segundo archivo (`hmi_interface.py`) está la interfaz gráfica que hicimos para poder interactuar con el robot de una forma más fácil y visual. La clase `RobotHMI` también es un nodo, y lo que hace principalmente es modelar el robot de forma virtual (como una simulación) y preparar la comunicación con los otros nodos. En su función `__init__`, se definen las características del robot (como su forma y dimensiones) y se crean los canales necesarios para enviar poses y recibir los ángulos reales. De esta forma, el robot real y la interfaz pueden estar siempre sincronizados.

Dentro de esa clase, la función `callback` simplemente guarda los valores que le llegan desde el nodo que controla los motores. Esos valores representan los ángulos actuales del robot, y se usan después para dibujar el robot en la pantalla o mostrar los números al usuario.

La función `send_pose` es la que se encarga de tomar una pose  y enviarla. Primero convierte los valores en bits  a radianes. Luego envía esos valores a través de uno de los canales y también envía el número de la pose por otro canal, para que el nodo que mueve los motores sepa cuál debe ejecutar. Además, esta función actualiza el modelo del robot en la interfaz, para que se vea cómo va a quedar después del movimiento.

En la interfaz visual, que se construye con la clase `HMI`, hay una función `__init__` que es la que pone todos los elementos en la ventana: se muestra el logo, los nombres del grupo, un menú para seleccionar una pose, un botón para enviarla, la vista 3D del robot, los ángulos actuales, y también un texto con todas las poses disponibles. También se pone un temporizador que cada medio segundo actualiza la vista 3D con los datos reales.

La función `send_pose` de esta clase se activa cuando el usuario hace clic en el botón "Enviar Pose". Lo que hace es mirar qué opción se eligió en el menú. Si es una pose válida, se la pasa al nodo que maneja el robot. Si se elige "Apagar Torque", se manda un `-1` para que el otro nodo entienda que debe apagar los motores.

La función `format_all_poses` es una función que simplemente arma un texto con todas las poses guardadas, para que el usuario pueda verlas claramente en la interfaz sin tener que buscar en el código.

Finalmente, la función `update_view` es la que mantiene actualizada la vista 3D. Esta función se ejecuta automáticamente cada 500 milisegundos y dibuja el robot en su estado actual, usando los ángulos que recibe desde el nodo que controla los motores. También actualiza los números que muestran cuánto está girada cada articulación.


### Plano de planta (Fisica)

![WhatsApp Image 2025-07-11 at 4 27 26 PM](https://github.com/user-attachments/assets/233fdfba-aec5-47fc-89e7-ff304fa8309f)

Se definen algunas distancias que podrían o no afectar las trayectorias por obstaculos.
![WhatsApp Image 2025-07-14 at 3 19 22 PM](https://github.com/user-attachments/assets/f9fde4af-e041-43ee-918f-8640ad8ba0e5)

![WhatsApp Image 2025-07-14 at 3 19 21 PM](https://github.com/user-attachments/assets/c9b3d927-4888-4df5-9152-9d19f707165e)

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




## Video 
link: https://youtu.be/1uN3QfF-pU0
