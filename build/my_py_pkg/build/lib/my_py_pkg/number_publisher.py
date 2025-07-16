import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisher(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.publisher_ = self.create_publisher(Int64, "number", 10)
        self.timer_ = self.create_timer(0.5, self.publish_counter)
        self.counter_ = 0
        self.get_logger().info("Number Publisher has been started")
    
    def publish_counter(self):
        msg = Int64()
        msg.data = self.counter_
        self.publisher_.publish(msg)
        self.get_logger().info("data: " + str(self.counter_))
        self.counter_ += 1


def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()