import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.subscriber_ = self.create_subscription(Int64, "number", self.callback_counter, 10)
        self.get_logger().info("number client has been started")

    def callback_counter(self, msg: Int64):
        self.get_logger().info("data: " + str(msg.data))

def main():
    rclpy.init()
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()