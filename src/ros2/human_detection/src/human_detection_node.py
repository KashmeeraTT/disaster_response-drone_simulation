import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class HumanDetectionNode(Node):
    def __init__(self):
        super().__init__('human_detection_node')
        self.image_subscriber = self.create_subscription(
            Image, '/camera/image_raw', self.image_callback, 10)
        self.bridge = CvBridge()

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        detected = self.detect_human(image)
        if detected:
            self.get_logger().info("Human detected!")

    def detect_human(self, image):
        # Placeholder for human detection logic, use OpenCV, YOLO, etc.
        return False  # No human detected in this example

def main(args=None):
    rclpy.init(args=args)
    node = HumanDetectionNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
