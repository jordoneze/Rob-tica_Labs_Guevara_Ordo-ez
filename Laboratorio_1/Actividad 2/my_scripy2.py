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
        self.timer = self.create_timer(0.1, self.get_input_and_draw)

        self.letters_drawn = False

    def get_input_and_draw(self):
        if not self.letters_drawn:
            self.letters_drawn = True
        
            letter = input("Ingresa una letra (C, E, G, J, M, O, S, X): ").upper()
            
            self.reset_position()
            time.sleep(0.5)
            self.clear_background()

            if letter == 'C':
                self.draw_c()
            elif letter == 'E':
                self.draw_e()
            elif letter == 'G':
                self.draw_g()
            elif letter == 'J':
                self.draw_j()
            elif letter == 'M':
                self.draw_m()
            elif letter == 'O':
                self.draw_o()
            elif letter=='S':
                self.draw_s()
            elif letter=='X':
                self.draw_x()  
            else:
                print("Letra no válida.")
            
            self.letters_drawn = False
            

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

    def draw_c(self):
        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 3.141  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 4.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

    def draw_e(self):
        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 3.141  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)


        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 1.5  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 3.142  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 1.5  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

    def draw_g(self):
        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.7  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 3.141  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.7  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 4.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

    def draw_j(self):
        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 1.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 4.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 1.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 3.142  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
    def draw_m(self):
        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 4.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -2.356  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -2.357 # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 4.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)


    def draw_o(self):
        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 4.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 4.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
    
    def draw_s(self):
        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -1.571  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 2.0  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
    
    def draw_x(self):
        self.get_logger().info('Moviendo la tortuga')
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 1.107  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)          
        
        msg = Twist()
        msg.linear.x = 4.472  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)
        
        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 3.142  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.236 # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = -2.219  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 2.236 # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 0.0  # Velocidad hacia adelante
        msg.angular.z = 3.142  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)

        msg = Twist()
        msg.linear.x = 4.472  # Velocidad hacia adelante
        msg.angular.z = 0.0  # Rotación
        self.publisher.publish(msg)
        time.sleep(1)


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
