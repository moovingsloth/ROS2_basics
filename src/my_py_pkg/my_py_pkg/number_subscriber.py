import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.get_logger().info("number_counter has been started")
        self.subscriber_ = self.create_subscription(Int64, "number", self.callback_counter, 10)
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.timer_ = self.create_timer(0.5, self.publish_counter)
        self.counter_ = 0

    def callback_counter(self):
        self.get_logger().info()("number")

    def publish_counter(self):
        msg = Int64()
        msg.data = self.counter_
        self.publisher_.publish(msg)
        self.counter_ += 2
        # self.get_logger().info("data: " + str(self.counter_))

def main():
    rclpy.init()
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()