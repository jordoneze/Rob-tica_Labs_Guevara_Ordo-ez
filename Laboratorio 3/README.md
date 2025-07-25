
# Laboratorio No. 03 - Robótica Industrial - Análisis y Operación del Manipulador Motoman MH6

## Cuadro comparativo Motoman MH6 y el IRB140.


|    | IRB140 | Motoman MH6 |
| :---:| :---: | :---: |
| Carga Máxima | 6 kg | 6 kg |
| Alcance | 0.8 m| 1.42 m|
| Número de grados de libertad | 6 | 8* |
| Velocidad | La velocidad cambia según la fuente de alimentación y el eje:  Para el eje 1 y 2 con trifasica son 200°/s, para el eje 3 con trifasica son 260°/s, para el eje 4 y 5 con trifasica son 360°/s y para el eje 6 con trifasica son 450°/s; para el eje 1 y 2 con monofasica son 200°/s, para el 3 con monofasica son 245°/s, para el 4 con monofasica son 348°/s, , para el 5 con monofasica son 360°/s y para el 6 con monofasica son 450°/s| La velocidad cambia según la articulación:  Para el eje 1 y 3 son 220°/s, para el eje 2 son 200°/s, para el eje 4 y 5 son 410°/s y para el eje 6 son 610°/s.|
|  | Resolución: Aproximadamente 0.01° en cada eje. Repetibilidad: 0.03 mm  | Repetibilidad: ±0.08 mm |
| Aplicaciones típicas | Esta diseñado especificamente para industrias manufactureras que utilizan automatización flexible basada en robots. Ensamblado, Dispensado, Manipulación de materiales, TCP remoto. | Robots de soldadura por arco, robots de ensamblaje, robots de dispensación, robots de moldeo por inyección, robots de manejo de maquinaria, robots de manipulación de materiales, robots de embalaje |
| Tipos de actuadores | AC servomotor + reductor + freno | AC servomotor + reductor + freno |
| Peso del manipulador| 98 kg | 130 kg |
| Consumo energético máximo| 0.44 kW a máxima velocidad [mm/s]  | 1.5 kVA |

*En especifico el Motoman MH6 que se encuentra en el laboratorio

## Home1 y Home2


Para la descripción de las posiciones de Home, se usa la posición de cada articulación, cuyos nombres se asocian a continuación:

![image](https://github.com/user-attachments/assets/0329f5e2-8fde-478d-abf1-c378bfb5a002)
### Home1
También se denomina Work Home Position. 

| Articulación | Posición |
| :---: | :---: |
| S | 0.0000 |
| L | 88.6629 |
| U | -81.0787 |
| R | -0.0017 |
| B | 51.7618 |
| T | -3.2709 |

![WhatsApp Image 2025-06-26 at 9 12 46 PM](https://github.com/user-attachments/assets/c564c2b9-10ad-4d64-8391-44811647a643)
![WhatsApp Image 2025-06-26 at 9 02 15 PM](https://github.com/user-attachments/assets/0c9fb2bc-7951-4095-b8b0-bdd0a817cb46)


### Home2

| Articulación | Posición |
| :---: | :---: |
| S | 0 |
| L | 0 |
| U | 0 |
| R | 0 |
| B | 0 |
| T | 0 |

![WhatsApp Image 2025-06-26 at 9 12 46 PM (1)](https://github.com/user-attachments/assets/643e8336-69ec-4517-ab4a-8f36d109d0a1)
![WhatsApp Image 2025-06-26 at 9 02 16 PM](https://github.com/user-attachments/assets/cbb04964-cbcc-4766-988a-2f30364131a6)

Home1 es la posición que se suele usar como referencia para el planteamiento de las trayectorias, por lo que es mejor para estas ocasiones y para referencia en mantenimiento, por otra parte Home2 es una posición más compacta, que ocupa menor volumen y es usado para mayor seguridad en el arranque o encendido. 

## Movimientos Manuales

Para poder realizar movimientos manuales, se incia encendiendo:
En el cofre general, se energizan los brakers correspondientes al robot Motoman, en el cofre totalizador del robot, se energiza el breaker totalizador y se verifica que haya tensión, posteriormente se energiza el controlador DX100 Yaskawa del robot girando la perilla adecuada en sentido horario. Después se quita la parada de emergencia girando el botón de emergencia en sentido horario. Con la llave en el Teach Pendant se pone en modo "teach" y se ubica en el menú del robot "second home position" y se oprimen los botones Servo On Ready, Fast, Freno y FWD, además se mantiene oprimido el boton de hombre muerto.
Para realizar movimientos articulares se necesita tener "Servo On" encendido, mantener el botón de hombre muerto oprimido y oprimir los botones según el movimiento que se desee en las articulaciones. Con el botón "COORD" se puede cambiar de sistema de referencia, asimismo se puede cambiar el tipo de movimiento entre articular y lineal, verificando para el movimiento que los servomotores esten activos y el botón de hombre muerto oprimido.  

Los botones para el movimiento son: 

![image](https://github.com/user-attachments/assets/cc82e10f-9118-49a8-940d-d69564b66e5e)

A la izquierda se encuentran los de movimiento lineal en los ejes del sistema de trabajo, a la derecha los giros en los ejes. También los botones de la izquierda y derecha funcionan para el movimiento de las articulaciones según las letras asignadas a cada una de las articulaciones, como se mostro anteriormente.
Para verificar el sistema de referencia, se observa en la parte superior de la pantalla.
![WhatsApp Image 2025-06-26 at 9 12 46 PM (2)](https://github.com/user-attachments/assets/ecfa9917-6a92-46d9-9da4-6a3420869632)


## Niveles de Velocidad
<!--Explicación completa sobre los niveles de velocidad para movimientos manuales, el proceso para cambiar entre niveles y cómo identificar el nivel establecido en la interfaz del robot.-->
Una vez el controlador se encuentra energizado nos dirigimos a tomar el teach pendant, en él existen tres botones donde cada uno tiene configurado un estado que define un rango de velocidades para cada uno, estos estados son: 

• High speed 

• fast

• slow
<!--Detallar los niveles de velocidad del Motoman para movimientos manuales y su configuración, ¿Cómo se hace
el cambio entre niveles de velocidad?, ¿C´omo se identifica en la pantalla el nivel de velocidad establecido?-->
Para cambiar entre niveles de velocidad solo basta con girar la llave, que se encuentra en la parte superior izquierda del teach pendant, hasta posicionarla en configuración 'TEACH'. Luego se escoge una de las 3 configuraciones mencionadas anteiormente presionando el botón correspondiente. 


[![Blank-2-Grids-Collage.png](https://i.postimg.cc/hPSsSsTH/Blank-2-Grids-Collage.png)](https://postimg.cc/mh5CjQdw)


Dentro de cualquiera de estos tres estados podremos movernos en unos rangos de velocidad que dependen del estado en el cual nos encontremos, claramente, siendo 'HIGH SPEED' el estado  con un rango de velocidades más alto que al 'FAST' y 'SLOW. Estos rangos de velocidad en un mismo estado podemos modificarlos presionando el mismo botón, lo que generará un salto de velocidad pequeño pero muy perceptible, cada estado tiene 3 niveles de velocidad que se controlan de esta manera y que pueden visualizarse en la parte superior de la interfaz con  una letra, que define el estado o modo en el que se encuentra  y 3 barras a su lado indicando con color verde  si se encuentra en el nivel 1, 2 o 3. 


[![niveles-Velocidad.png](https://i.postimg.cc/XYT4SpmD/niveles-Velocidad.png)](https://postimg.cc/pmYgKX2D)


# RoboDK: Funcionalidades y Comunicación con Manipuladores Motoman
<!--Descripción de las principales funcionalidades de RoboDK, explicando cómo se comunica con el manipulador Motoman y qué procesos realiza para ejecutar movimientos.
Explicar las aplicaciones principales de RoboDK y cómo se comunica con el manipulador, ¿Qué hace RoboDK
para mover el manipulador-->


## RoboDK

RoboDK es un software de simulación y programación offline para robots industriales que permite crear, simular y generar programas de robot sin necesidad de interrumpir la producción. Es una plataforma versátil que soporta más de 500 modelos de robots de diferentes fabricantes, incluyendo los manipuladores Motoman de Yaskawa.


## Comunicación con Manipuladores Motoman

### Arquitectura de Comunicación

RoboDK se comunica con los manipuladores Motoman a través de varios métodos y protocolos:

#### 1. Controlador DX100/YRC1000
- **Ethernet/IP**: Protocolo industrial estándar para comunicación en tiempo real
- **TCP/IP Socket**: Comunicación directa a través de red Ethernet
- **Archivos de programa**: Transferencia de programas generados en formato JBI (Job Binary Instruction)

#### 2. Driver Específico para Motoman
RoboDK incluye un driver especializado que:
- Traduce comandos de RoboDK al lenguaje nativo INFORM del controlador Motoman
- Gestiona la comunicación bidireccional entre el software y el controlador
- Maneja estados del robot (posición actual, alarmas, modo de operación)

### 3. Interfaz de Programación (API)
- **Python API**: Permite integración personalizada y automatización avanzada
- **C# y LabVIEW**: Soporte para diferentes entornos de desarrollo
- **ROS Integration**: Compatibilidad con Robot Operating System

## Procesos para Ejecutar Movimientos

### 1. Planificación de Trayectorias
RoboDK realiza los siguientes pasos para planificar movimientos:

**Análisis Cinemático**:
- Calcula la cinemática inversa para determinar ángulos de articulaciones
- Verifica límites de movimiento de cada eje
- Optimiza configuraciones del robot 

**Generación de Trayectorias**:
- Interpola puntos intermedios entre posiciones objetivo
- Aplica perfiles de velocidad y aceleración suavizados
- Considera limitaciones dinámicas del robot

### 2. Traducción de Comandos
El proceso de traducción incluye:

**De RoboDK a INFORM**:
- Convierte coordenadas cartesianas a coordenadas de articulaciones
- Traduce comandos de movimiento (MoveJ, MoveL, MoveC) al formato JBI
- Incorpora parámetros de velocidad, precisión y configuración



### 3. Ejecución en el Controlador
Una vez transferido el programa:
- El controlador Motoman ejecuta las instrucciones INFORM
- Controla servo-motores de cada articulación
- Monitorea sensores de posición y fuerza
- Reporta estado de ejecución a RoboDK

**Simulación de robots**:
RoboDK permite simular el movimiento de robots industriales en un entorno virtual 3D, lo que ayuda a verificar el alcance, la cinemática y la ausencia de colisiones antes de ejecutar cualquier programa en el mundo real.

**Generación automática de trayectorias**:
El software puede generar trayectorias de forma automática a partir de modelos CAD o puntos definidos, optimizando los movimientos del robot para tareas como corte, pintura, soldadura o inspección.

**Programación offline** :
Permite crear, editar y depurar programas de robot sin necesidad de estar conectado físicamente a la máquina, lo que reduce el tiempo de parada en la producción.

**Exportación de programas nativos**:
RoboDK genera código específico para el controlador del robot (como archivos .JBI para Yaskawa), asegurando compatibilidad total con el hardware real y evitando errores por traducción de lenguaje.

**Integración con software CAD/CAM**:
Es posible importar  archivos de SolidWorks, Inventor, Fusion 360, Rhino, entre otros, para generar trayectorias basadas en geometría real, facilitando la automatización de procesos basados en diseño.

**Calibración de robots y herramientas**:
RoboDK ofrece módulos para calibrar la base del robot, herramientas (TCP) y sistemas de visión, mejorando la precisión del robot en su entorno de trabajo real.

**Simulación de sensores y periferia**:
Es posible integrar , cintas transportadoras, herramientas, objetos, y otros dispositivos virtuales para simular una sistema de trabajo completo.

**Control en tiempo real del robot**:
 RoboDK permite enviar comandos y mover el robot en tiempo real directamente desde el entorno virtual.

## Ventajas de la Integración RoboDK-Motoman

### 1. Eficiencia Operacional
Ya que permite hacer cambios rápidos y seguros en los procesos sin detener la producción, gracias a su capacidad de probar virtualmente cada modificación. En conjunto, esto reduce costos de programación, mejora la precisión operativa y permite una mayor flexibilidad en la línea de producción.s

### 2. Precisión 
Si bien puede no igualar la precisión milimétrica que ofrecen plataformas desarrolladas exclusivamente para marcas específicas, como es el caso de RoboStudio para ABB, RoboDK mantiene un balance eficiente entre precisión suficiente para la mayoría de procesos industriales y facilidad de uso. Además, al generar programas nativos en formato JBI para el controlador Yaskawa, asegura que las trayectorias planificadas se ejecuten con un margen de error mínimo

### 3. Flexibilidad y Escalabilidad
RoboDK ofrece una alta flexibilidad y escalabilidad al trabajar con un robot Motoman MH6 porque no está limitado a un solo fabricante ni a un entorno cerrado, lo que permite adaptar rápidamente el sistema a distintos procesos, configuraciones o cambios en la línea de producción.






# Análisis Comparativo: RoboDK vs RobotStudio

RoboDK y RobotStudio son dos de las herramientas de simulación y programación offline más importantes en el ámbito de la robótica industrial. Aunque ambas comparten el objetivo común de facilitar la programación y simulación de robots, representan objetivos y enfoques diferentes que las hacen más adecuadas para distintos tipos de aplicaciones y usuarios.

## ¿Qué es cada herramienta?

### RoboDK
RoboDK representa flexibilidad y escalabilidad  en la automatización industrial. El objetivo central de este software es poder abarcar todo el mercado de robots compormetiendose con las empresas a nivel mundial a brindar un soporte acerca de cualquier proceso industrial que deseen realizar, si sus limitaciones de precisión y modelado lo permiten.  

### RobotStudio
RobotStudio, desarrollado por ABB . Es la herramienta que lleva la simulación de robots ABB a su máxima rendimiento, ofreciendo un nivel de detalle y funcionalidad que solo es posible cuando el fabricante del software es el mismo que el del hardware. 

## Tabla Comparativa - Aspectos Más Relevantes

| Criterio | RoboDK | RobotStudio |
|----------|---------|-------------|
| **Compatibilidad** | 500+ robots (50+ marcas) | Solo robots ABB |
| **Costo** | Licencia comercial  | Gratuito (versión básica) |
| **Curva de aprendizaje** | Moderada (2-4 semanas) | Alta (1-3 meses) |
| **Precisión simulación** | ±0.1mm | ±0.05mm |
| **Programación** | Python, C#, MATLAB, LabVIEW | RAPID (nativo ABB) |
| **Aplicación principal** | Entornos multi-marca | Especialización ABB |
| **Integración** | Multi-protocolo | Ecosistema ABB completo |
| **ROI típico** | 6-12 meses | 3-8 meses (con ABB) |
| **Soporte** | Comercial estándar | ABB mundial |

## Ventajas y Limitaciones

### RoboDK
| Ventajas | Limitaciones |
|----------|-------------|
|  Universalidad multi-marca |  Menor especialización por robot |
|  Interfaz intuitiva |  Costo por licencia de robot |
|  APIs múltiples (Python, C#, etc.) |  Funciones específicas limitadas |
|  Flexibilidad de integración |  Optimización genérica |

### RobotStudio 
| Ventajas | Limitaciones |
|----------|-------------|
|  Máxima precisión (±0.05mm) |  Solo robots ABB |
|  Integración nativa ABB |  Curva de aprendizaje alta |
|  Gratuito (versión básica) |  Vendor lock-in |
|  Simulación 1:1 con robot real |  Interfaz compleja |

## Aplicaciones óptimas para utilizar RobotStudio 

 •Comisionamiento virtual completo (RAPID + señales)
 
• Simulación exacta de tiempos y comportamiento real

 •Sincronización de robots ABB
 
 •Testeo de seguridad y Smart Components
 
• Proyectos de automatización compleja

•Entrenamiento profesional en ABB

## Aplicaciones óptimas para utilizar RoboDK
• Fresado/mecanizado (Programación CAM avanzada)

• Simulación de trayectorias sencillas (pintura, soldadura, pick & place)

• Generación de programas básicos ABB

•Escalabilidad y adaptación de procesos con multiples Robots




## Trayectoria Planteada 
![image](https://github.com/user-attachments/assets/6214e048-4f28-4e0f-b923-85be6c8b2a8c)
![image](https://github.com/user-attachments/assets/248b9236-2797-4c0e-874f-363f2962961e)


## Video 

**Link** :https://youtu.be/9D8tAegWrG0
