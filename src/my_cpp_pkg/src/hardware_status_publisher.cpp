#include "rclcpp/rclcpp.hpp"
#include "my_robot_interfaces/msg/hardware_status.hpp"

class HardwareStatusPublisherNode : public rclcpp::Node
{
public:
  HardwareStatusPublisherNode() : Node("hardware_status_publisher")
  {
    publisher_ = this->create_publisher<my_robot_interfaces::msg::HardwareStatus>("hardware_status", 10);
    timer_ = this->create_wall_timer(
      std::chrono::seconds(1),
      std::bind(&HardwareStatusPublisherNode::publishHardwareStatus, this)
    );
  }

private:
  void publishHardwareStatus()
  {
    auto msg = my_robot_interfaces::msg::HardwareStatus();
    msg.temperature = 57.2;
    msg.are_motors_ready = false;
    msg.debug_message = "Motos are too hot";
    publisher_->publish(msg);
  }
  rclcpp::Publisher<my_robot_interfaces::msg::HardwareStatus>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<HardwareStatusPublisherNode>());
  rclcpp::shutdown();
  return 0;
}
