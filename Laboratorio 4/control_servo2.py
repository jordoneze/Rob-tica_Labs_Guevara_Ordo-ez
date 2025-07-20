# pincher_control/control_servo.py
import rclpy
from rclpy.node import Node
from dynamixel_sdk import PortHandler, PacketHandler
from std_msgs.msg import Float32MultiArray, Int32
import time
import math

# Direcciones del AX-12A
ADDR_TORQUE_ENABLE    = 24
ADDR_GOAL_POSITION    = 30
ADDR_MOVING_SPEED     = 32
ADDR_TORQUE_LIMIT     = 34
ADDR_PRESENT_POSITION = 36

positions = [
    [512, 512, 512, 512, 512],  # Home
    [583, 583, 568, 454, 512],
    [412, 611, 426, 597, 512],
    [753, 454, 668, 583, 512],
    [739, 412, 668, 384, 512]
]

class PincherController(Node):
    def __init__(self):
        super().__init__('pincher_controller')

        # Declarar parámetros solo una vez
        self.declare_parameter('port', '/dev/ttyUSB0')
        self.declare_parameter('baudrate', 1000000)
        self.declare_parameter('dxl_ids', [1, 2, 3, 4, 5])
        self.declare_parameter('moving_speed', 100)
        self.declare_parameter('torque_limit', 800)
        self.declare_parameter('delay', 2.0)

        # Obtener parámetros
        self.port_name     = self.get_parameter('port').value
        self.baudrate      = self.get_parameter('baudrate').value
        self.dxl_ids       = self.get_parameter('dxl_ids').value
        self.moving_speed  = self.get_parameter('moving_speed').value
        self.torque_limit  = self.get_parameter('torque_limit').value
        self.delay_seconds = self.get_parameter('delay').value

        # Inicializar comunicación
        self.port = PortHandler(self.port_name)
        self.joint_pub = self.create_publisher(Float32MultiArray, 'joint_angles', 10)

        if not self.port.openPort():
            self.get_logger().error('No se pudo abrir el puerto.')
            rclpy.shutdown()
            return

        self.port.setBaudRate(self.baudrate)
        self.packet = PacketHandler(1.0)

        # Suscripción al índice de movimiento desde HMI
        self.subscription = self.create_subscription(
            Int32,
            'move_index',
            self.callback_move_index,
            10
        )

    def mover_a_posicion(self, goal_positions):
        if len(goal_positions) != len(self.dxl_ids):
            self.get_logger().error('Las longitudes de goal_positions y dxl_ids no coinciden.')
            return

        for dxl_id, goal in zip(self.dxl_ids, goal_positions):
            self.packet.write2ByteTxRx(self.port, dxl_id, ADDR_TORQUE_LIMIT, self.torque_limit)
            self.packet.write2ByteTxRx(self.port, dxl_id, ADDR_MOVING_SPEED, self.moving_speed)
            self.packet.write1ByteTxRx(self.port, dxl_id, ADDR_TORQUE_ENABLE, 1)
            self.packet.write2ByteTxRx(self.port, dxl_id, ADDR_GOAL_POSITION, goal)
            self.get_logger().info(f'[ID {dxl_id}] → goal={goal}')

        for dxl_id in self.dxl_ids:
            pos, _, _ = self.packet.read2ByteTxRx(self.port, dxl_id, ADDR_PRESENT_POSITION)
            self.get_logger().info(f'[ID {dxl_id}] posición actual={pos}')

        self.get_logger().info(f'Esperando {self.delay_seconds}s...')
        time.sleep(self.delay_seconds)
        angles_msg = Float32MultiArray()
        angles_radians = [((val-512) * 300.0 / 1023.0) * math.pi / 180.0 for val in goal_positions]
        angles_msg.data = angles_radians
        self.joint_pub.publish(angles_msg)

    def callback_move_index(self, msg):
        index = msg.data
        if index == -1:
         self.get_logger().info("Recibido comando para APAGAR TORQUE.")
         for dxl_id in self.dxl_ids:
             self.packet.write1ByteTxRx(self.port, dxl_id, ADDR_TORQUE_ENABLE, 0)
         return
        if 0 <= index < len(positions):
            self.get_logger().info(f"Recibido comando de movimiento a la posición {index+1}")
            self.mover_a_posicion(positions[index])
        else:
            self.get_logger().warn(f"Índice inválido recibido: {index}")


def main(args=None):
    rclpy.init(args=args)
    node = PincherController()
    rclpy.spin(node)
    node.port.closePort()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
