from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='human_detection',
            executable='human_detection_node',
            name='human_detection_node',
            output='screen'),
    ])
