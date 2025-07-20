import sys
import math
from roboticstoolbox.backends.swift import Swift
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QPushButton, QHBoxLayout, QGridLayout, QComboBox
)
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtGui import QPixmap

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, Int32
import roboticstoolbox as rtb
from dynamixel_sdk import PortHandler, PacketHandler
from PyQt5.QtCore import QTimer, Qt


# Direcciones del AX-12A
ADDR_TORQUE_ENABLE    = 24
ADDR_GOAL_POSITION    = 30
ADDR_MOVING_SPEED     = 32
ADDR_TORQUE_LIMIT     = 34
ADDR_PRESENT_POSITION = 36

class RobotHMI(Node):
    def __init__(self):
        super().__init__('robot_hmi')
        
        self.robot = rtb.DHRobot([
            rtb.RevoluteDH(a=0.0, alpha=np.pi/2, d=0.042, offset=0),
            rtb.RevoluteDH(a=0.104, alpha=0.0, d=0.0, offset=np.pi/2),
            rtb.RevoluteDH(a=0.2, alpha=0.0, d=0.0, offset=0),
            rtb.RevoluteDH(a=0.0, alpha=np.pi/2, d=0.0, offset=np.pi/2),
            rtb.RevoluteDH(a=0.0, alpha=0.0, d=0.1, offset=0)
            
        ])

        self.joint_angles = [0.0] * 5
        self.publisher = self.create_publisher(Float32MultiArray, 'joint_angles', 10)
        self.command_pub = self.create_publisher(Int32, 'move_index', 10)  # para enviar índice de movimiento
        self.subscriber = self.create_subscription(Float32MultiArray, 'joint_angles', self.callback, 10)
        
        # Parámetros para Dynamixel
        self.declare_parameter('port', '/dev/ttyUSB0')
        self.declare_parameter('baudrate', 1000000)
        self.declare_parameter('dxl_ids', [1, 2, 3, 4, 5])
        self.declare_parameter('moving_speed', 100)
        self.declare_parameter('torque_limit', 800)

        self.port_name     = self.get_parameter('port').value
        self.baudrate      = self.get_parameter('baudrate').value
        self.dxl_ids       = self.get_parameter('dxl_ids').value
        self.moving_speed  = self.get_parameter('moving_speed').value
        self.torque_limit  = self.get_parameter('torque_limit').value

        self.port = PortHandler(self.port_name)
        if not self.port.openPort():
            self.get_logger().error('No se pudo abrir el puerto.')
            rclpy.shutdown()
            return
        self.port.setBaudRate(self.baudrate)
        self.packet = PacketHandler(1.0)

    def callback(self, msg):
        if len(msg.data) == 5:
            self.joint_angles = msg.data

    def send_pose(self, pose_raw, pose_index):
        radians = [((val-512) * 300.0 / 1023.0) * math.pi / 180.0 for val in pose_raw]
        msg = Float32MultiArray()
        msg.data = radians
        self.publisher.publish(msg)

        idx_msg = Int32()
        idx_msg.data = pose_index
        self.command_pub.publish(idx_msg)

        # Mostrar en Swift
        self.robot.q = radians
        self.swift.step()  # Actualiza la vista


class HMI(QWidget):
    def __init__(self, ros_node):
        super().__init__()
        self.setWindowTitle('Interfaz HMI - Manipulador')
        self.resize(900, 700)
        self.ros_node = ros_node
        
        main_layout = QVBoxLayout()
        logo_label = QLabel()
        pixmap = QPixmap("/home/stivenguevara/Downloads/images.png")  # ← Cambia esto por la ruta real
        pixmap = pixmap.scaledToWidth(150)    # Escala opcionalmente
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignRight)
        main_layout.addWidget(logo_label)

        info_label = QLabel('Grupo: Robótica 2025-1\nIntegrantes: Stivens Camilo Guevara, Jeny Ximena Ordoñez\nIngeniería Mecatrónica \nUniversida Nacional de Colombia')
        main_layout.addWidget(info_label)

        self.canvas = FigureCanvas(Figure())
        main_layout.addWidget(self.canvas)
        fig = Figure(figsize=(22, 25), dpi=100)  # puedes ajustar el tamaño aquí
        self.canvas = FigureCanvas(fig)
        main_layout.addWidget(self.canvas)
        self.ax = self.canvas.figure.add_subplot(111, projection='3d')

        self.poses = [
            [512, 512, 512, 512, 512],
            [583, 583, 568, 454, 512],
            [412, 611, 426, 597, 512],
            [753, 454, 668, 583, 512],
            [739, 412, 668, 384, 512]
        ]

        combo_layout = QHBoxLayout()
        self.pose_selector = QComboBox()
        for i in range(len(self.poses)):
            self.pose_selector.addItem(f'Pose {i+1}')
        self.pose_selector.addItem('Apagar Torque')

        send_button = QPushButton('Enviar Pose')
        send_button.clicked.connect(self.send_pose)
        combo_layout.addWidget(self.pose_selector)
        combo_layout.addWidget(send_button)
        main_layout.addLayout(combo_layout)

        self.angle_labels = [QLabel(f'Articulación {i+1}: 0.0 rad') for i in range(5)]
        for label in self.angle_labels:
            main_layout.addWidget(label)

        self.pose_list_label = QLabel()
        self.pose_list_label.setText(self.format_all_poses())
        self.pose_list_label.setAlignment(Qt.AlignRight)
        self.pose_list_label.setStyleSheet("font-family: monospace;")
        main_layout.addWidget(self.pose_list_label)  
        self.setLayout(main_layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_view)
        self.timer.start(500)
        
    def send_pose(self):
        idx = self.pose_selector.currentIndex()
        if idx < len(self.poses):
            raw_pose = self.poses[idx]
            self.ros_node.send_pose(raw_pose, idx)
        else:
            # Enviar señal especial -1 para apagar torque
            from std_msgs.msg import Int32
            msg = Int32()
            msg.data = -1
            self.ros_node.command_pub.publish(msg)
            
    def format_all_poses(self):
        text = "Poses predefinidas (valores crudos):\n"
        for i, pose in enumerate(self.poses):
            text += f"Pose {i+1}: {pose}\n"
        return text

    def update_view(self):
            self.ax.cla()
            try:
                q = np.array(self.ros_node.joint_angles, dtype=float)
                self.ros_node.robot.plot(q, block=False)
                T_all = self.ros_node.robot.fkine_all(q)
                xs, ys, zs = [], [], []
                for T in T_all:
                    pos = T.t
                    xs.append(pos[0])
                    ys.append(pos[1])
                    zs.append(pos[2])

                self.ax.plot(xs, ys, zs, marker='o')
                self.ax.set_xlim([-0.6, 0.6])
                self.ax.set_ylim([-0.6, 0.6])
                self.ax.set_zlim([0, 0.8])
                self.ax.set_xlabel('X')
                self.ax.set_ylabel('Y')
                self.ax.set_zlabel('Z')
            except Exception as e:
                print(f"Error al graficar: {e}")
            for i, angle in enumerate(self.ros_node.joint_angles):
                self.angle_labels[i].setText(f'Articulación {i+1}: {angle:.2f} rad')
            self.canvas.draw()

# -------------------- EJECUCIÓN --------------------
def main():
    rclpy.init()
    node = RobotHMI()
    app = QApplication(sys.argv)
    gui = HMI(node)
    gui.show()

    timer = QTimer()
    timer.timeout.connect(lambda: rclpy.spin_once(node, timeout_sec=0.1))
    timer.start(100)

    app.exec_()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
