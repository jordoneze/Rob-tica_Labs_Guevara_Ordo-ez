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
Una vez el el controlador se encuentra energizado nos dirigimos a tomar el teach pendant, en él existen tres botones donde cada uno tiene configurado un estado que define un rango de velocidades para cada uno, estos estados son : 

• High speed 

• fast

• slow
<!--Detallar los niveles de velocidad del Motoman para movimientos manuales y su configuración, ¿Cómo se hace
el cambio entre niveles de velocidad?, ¿C´omo se identifica en la pantalla el nivel de velocidad establecido?-->
Para cambiar entre niveles de velocidad solo basta con girar la llave, que se encuentra en la parte superior izquierda del teach pendant, hasta posicionarla en configuración 'TEACH'. Luego se escoge una de las 3 configuraciones mencionadas anteiormente presionando el botón correspondiente. 


[![Blank-2-Grids-Collage.png](https://i.postimg.cc/hPSsSsTH/Blank-2-Grids-Collage.png)](https://postimg.cc/mh5CjQdw)


Dentro de cualquiera de estos tres estados podremos movernos en unos rangos de velocidad que dependen del estado en el cual nos encontremos, claramente, siendo 'HIGH SPEED' el estado  con un rango de velocidades más alto que al 'FAST' y 'SLOW. Estos rangos de velocidad en un mismo estado podemos modificarlos presionando el mismo botón, lo que generará un salto de velocidad pequeño pero muy perceptible, cada estado tiene 3 niveles de velocidad que se controlan de esta manera y que pueden visualizarse en la parte superior de la interfaz con  una letra, que define el estado o modo en el que se encuentra  y 3 barras a su lado indicando con color verde  si se encuentra en el nivel 1, 2 o 3. 


[![niveles-Velocidad.png](https://i.postimg.cc/XYT4SpmD/niveles-Velocidad.png)](https://postimg.cc/pmYgKX2D)


## Funcionalidades de RoboDK
<!--Descripción de las principales funcionalidades de RoboDK, explicando cómo se comunica con el manipulador Motoman y qué procesos realiza para ejecutar movimientos.
Explicar las aplicaciones principales de RoboDK y cómo se comunica con el manipulador, ¿Qué hace RoboDK
para mover el manipulador-->
# RoboDK: Funcionalidades y Comunicación con Manipuladores Motoman

## Descripción General de RoboDK

RoboDK es un software de simulación y programación offline para robots industriales que permite crear, simular y generar programas de robot sin necesidad de interrumpir la producción. Es una plataforma versátil que soporta más de 500 modelos de robots de diferentes fabricantes, incluyendo los manipuladores Motoman de Yaskawa.

## Principales Funcionalidades de RoboDK

### 1. Simulación 3D Avanzada
- **Entorno virtual realista**: Permite crear estaciones de trabajo completas con modelos 3D precisos del robot, herramientas, piezas y entorno de trabajo
- **Detección de colisiones**: Identifica automáticamente posibles colisiones entre el robot, herramientas y obstáculos del entorno
- **Análisis de alcance**: Visualiza el espacio de trabajo del robot y verifica la accesibilidad a todas las posiciones requeridas

### 2. Programación Offline
- **Independencia de la producción**: Permite programar el robot sin detener las operaciones de producción
- **Múltiples lenguajes**: Genera código nativo para diferentes controladores de robot
- **Optimización automática**: Optimiza trayectorias para reducir tiempo de ciclo y desgaste del robot

### 3. Calibración y Medición
- **Calibración de herramientas**: Determina con precisión la posición y orientación de herramientas (TCP - Tool Center Point)
- **Calibración de piezas**: Establece sistemas de coordenadas precisos para las piezas de trabajo
- **Medición automática**: Utiliza sensores para verificar posiciones y dimensiones

## Comunicación con Manipuladores Motoman

### Arquitectura de Comunicación

RoboDK se comunica con los manipuladores Motoman a través de varios métodos y protocolos:

#### 1. Controlador DX200/YRC1000
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
- Optimiza configuraciones del robot (elbow up/down, wrist flip)

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

**Ejemplo de traducción**:
```
RoboDK: MoveL(Target_1, 100 mm/s)
INFORM: MOVL VJ=5.00 PL=0
```

### 3. Ejecución en el Controlador
Una vez transferido el programa:
- El controlador Motoman ejecuta las instrucciones INFORM
- Controla servo-motores de cada articulación
- Monitorea sensores de posición y fuerza
- Reporta estado de ejecución a RoboDK

## Aplicaciones Principales de RoboDK

### 1. Soldadura por Arco y Punto
- **Programación de cordones de soldadura**: Define trayectorias precisas para soldadura
- **Control de parámetros**: Gestiona velocidad de soldadura, corriente y voltaje
- **Simulación realista**: Visualiza el proceso de soldadura con efectos visuales

### 2. Mecanizado y Fresado
- **Importación de CAM**: Integra trayectorias de herramientas desde software CAM
- **Optimización de orientación**: Calcula orientaciones óptimas de herramientas
- **Control de velocidad de husillo**: Sincroniza movimiento del robot con herramientas rotativas

### 3. Paletizado y Manipulación
- **Generación automática de patrones**: Crea secuencias de paletizado automáticamente
- **Optimización de trayectorias**: Minimiza tiempo de ciclo en operaciones repetitivas
- **Control de herramientas**: Gestiona pinzas, ventosas y herramientas de sujeción

### 4. Inspección y Medición
- **Programación de rutinas de inspección**: Define secuencias de medición automatizadas
- **Integración de sensores**: Incorpora cámaras, láser y sensores táctiles
- **Análisis de resultados**: Procesa datos de medición y genera reportes

## Proceso Detallado: Cómo RoboDK Mueve el Manipulador

### Paso 1: Definición del Objetivo
1. **Especificación del target**: El usuario define posición y orientación objetivo
2. **Selección de herramienta**: Se especifica qué herramienta utilizar (TCP)
3. **Configuración de parámetros**: Velocidad, aceleración, precisión

### Paso 2: Cálculo Cinemático
1. **Cinemática inversa**: RoboDK calcula ángulos necesarios para cada articulación
2. **Verificación de límites**: Comprueba que todos los ángulos estén dentro de rangos permitidos
3. **Selección de configuración**: Elige la configuración óptima del robot

### Paso 3: Planificación de Movimiento
1. **Interpolación**: Genera puntos intermedios en la trayectoria
2. **Perfiles de velocidad**: Aplica aceleración y desaceleración suaves
3. **Verificación de colisiones**: Comprueba toda la trayectoria

### Paso 4: Generación de Código
1. **Traducción a INFORM**: Convierte comandos a lenguaje nativo Motoman
2. **Optimización**: Ajusta parámetros para eficiencia
3. **Formateo JBI**: Genera archivo ejecutable por el controlador

### Paso 5: Transferencia y Ejecución
1. **Transferencia de archivo**: Envía programa JBI al controlador via Ethernet
2. **Carga en memoria**: El controlador carga el programa
3. **Ejecución controlada**: El controlador ejecuta movimientos siguiendo las instrucciones
4. **Retroalimentación**: RoboDK recibe información de estado en tiempo real

## Ventajas de la Integración RoboDK-Motoman

### 1. Eficiencia Operacional
- Reducción significativa del tiempo de programación
- Eliminación de paradas de producción para programación
- Optimización automática de trayectorias

### 2. Precisión y Confiabilidad
- Simulación exacta antes de la ejecución real
- Detección preventiva de errores y colisiones
- Calibración precisa de herramientas y piezas

### 3. Flexibilidad y Escalabilidad
- Fácil reprogramación para nuevas aplicaciones
- Soporte para múltiples robots simultáneamente
- Integración con sistemas de manufactura existentes





## RoboDK y RobotStudio

Análisis comparativo entre RoboDK y RobotStudio, destacando ventajas, limitaciones y aplicaciones de cada herramienta.
# Análisis Comparativo: RoboDK vs RobotStudio

## Introducción

RoboDK y RobotStudio son dos de las herramientas de simulación y programación offline más importantes en el ámbito de la robótica industrial. Aunque ambas comparten el objetivo común de facilitar la programación y simulación de robots, representan filosofías y enfoques diferentes que las hacen más adecuadas para distintos tipos de aplicaciones y usuarios.

## ¿Qué Significa Cada Herramienta?

### RoboDK: La Plataforma Universal
RoboDK representa la **democratización de la programación robótica**. Es una herramienta que rompe las barreras entre diferentes marcas de robots, ofreciendo una plataforma unificada donde la programación se vuelve independiente del fabricante. Para mí, RoboDK simboliza la **flexibilidad y accesibilidad** en la automatización industrial.

**Objetivo central**: "Un software, múltiples robots"
- Enfoque multi-fabricante desde su concepción
- Simplicidad en la interfaz de usuario
- Democratización del acceso a la simulación robótica

### RobotStudio: La Excelencia Especializada
RobotStudio, desarrollado por ABB, representa la **perfección en la especialización**. Es la herramienta que lleva la simulación de robots ABB a su máxima expresión, ofreciendo un nivel de detalle y funcionalidad que solo es posible cuando el fabricante del software es el mismo que el del hardware.

**Objetivocentral**: "Máxima fidelidad para máximo rendimiento"
- Integración perfecta con el ecosistema ABB
- Simulación de alta fidelidad
- Herramientas avanzadas para aplicaciones complejas
# Análisis Comparativo: RoboDK vs RobotStudio


## Tabla Comparativa - Aspectos Más Relevantes

| Criterio | RoboDK | RobotStudio |
|----------|---------|-------------|
| **Compatibilidad** | 500+ robots (50+ marcas) | Solo robots ABB |
| **Costo** | Licencia comercial  | Gratuito (versión básica) |
| **Curva de aprendizaje** | Moderada (2-4 semanas) | Alta (1-3 meses) |
| **Precisión simulación** | ±0.1mm | ±0.05mm |
| **Programación** | Python, C#, MATLAB, LabVIEW | RAPID (nativo ABB) |
| **Aplicación principal** | Entornos multi-marca | Especialización ABB |
| **Velocidad simulación** | Rápida | Muy rápida |
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

## Aplicaciones óptimas para utilizar Robo Studio 

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

•Escalibilidad y adaptación de procesos con multiples Robots




## Trayectoria Planteada 
![image](https://github.com/user-attachments/assets/6214e048-4f28-4e0f-b923-85be6c8b2a8c)
![image](https://github.com/user-attachments/assets/248b9236-2797-4c0e-874f-363f2962961e)


## Video 

