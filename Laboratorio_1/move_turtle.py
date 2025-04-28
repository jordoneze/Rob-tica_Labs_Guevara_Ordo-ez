import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
import sys
import tty
import termios
import threading
import time
import math
from turtlesim.srv import TeleportAbsolute

class AutoDraw(Node):


    def __init__(self):
        super().__init__('auto_draw')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.clear_client = self.create_client(Empty, '/clear')
        self.teleport_client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        self.timer = self.create_timer(0.1, self.teleop_control)
        self.settings = termios.tcgetattr(sys.stdin)

        self.letters_drawn = False

    def teleop_control(self):
        print("Utilice las flechas para mover la tortuga.")
        
        while rclpy.ok():
            key = self.getKey()
            if key == '\x03':
                break
            elif key == '\x41': # Up arrow
                self.move_front()
            elif key == '\x42': # Down arrow
                self.move_back()
            elif key == '\x44': # Left arrow
                self.move_left()
            elif key == '\x43': # Right arrow
                self.move_right()
            
            

    def reset_position(self):
        while not self.teleport_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando servicio /turtle1/teleport_absolute...')
        request = TeleportAbsolute.Request()
        request.x = 5.5
        request.y = 5.5
        request.theta = 0.0
        self.teleport_client.call_async(request)

    def clear_background(self):
        while not self.clear_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando servicio /clear...')
        self.clear_client.call_async(Empty.Request())


    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self.settings)
        return key


    def move_left(self):
      msg = Twist()
      msg.linear.x = 0.0  # Velocidad hacia adelante
      msg.angular.z = 0.18  # Rotación
      self.publisher.publish(msg)
      time.sleep(1)
        
    def move_front(self):
        msg = Twist()
        msg.linear.x = 0.3  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

    def move_right(self):
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -0.18  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

    def move_back(self):
        msg = Twist()
        msg.linear.x = -0.3  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)







    def move_line(self, duration):
        twist = Twist()
        twist.linear.x = 1.0
        self.publisher.publish(twist)
        self.get_clock().sleep_for(rclpy.duration.Duration(seconds=duration))
        twist.linear.x = 0.0
        self.publisher.publish(twist)

    def rotate_turtle(self, angle_degrees):
        twist = Twist()
        twist.angular.z = 1.0 if angle_degrees > 0 else -1.0
        duration = abs(angle_degrees) / 45.0  # suponiendo 45 grados por segundo
        self.publisher.publish(twist)
        self.get_clock().sleep_for(rclpy.duration.Duration(seconds=duration))
        twist.angular.z = 0.0
        self.publisher.publish(twist)

    def move_circle_segment(self, start_angle, end_angle):
        twist = Twist()
        twist.linear.x = 1.0
        twist.angular.z = 1.0
        duration = abs(end_angle - start_angle) / 45.0
        self.publisher.publish(twist)
        self.get_clock().sleep_for(rclpy.duration.Duration(seconds=duration))
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = AutoDraw()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
