import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid
from slam_toolbox.srv import SaveMap

class SlamNode(Node):
    def __init__(self):
        super().__init__('slam_node')
        self.declare_parameter('map_topic', 'map')
        self.map_subscriber = self.create_subscription(
            OccupancyGrid, self.get_parameter('map_topic').value, self.map_callback, 10)
        self.create_timer(10, self.save_map)

    def map_callback(self, msg):
        self.get_logger().info("SLAM: Received a new map")

    def save_map(self):
        self.get_logger().info("Saving map...")
        save_map_client = self.create_client(SaveMap, 'save_map')
        req = SaveMap.Request()
        req.filename = 'map.pgm'
        future = save_map_client.call_async(req)

def main(args=None):
    rclpy.init(args=args)
    node = SlamNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
