from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'slam_config',
            default_value='config/slam_config.yaml',
            description='Path to the SLAM configuration file'
        ),
        
        Node(
            package='slam_toolbox',
            executable='slam_toolbox_node',
            name='slam_toolbox_node',
            output='screen',
            parameters=[LaunchConfiguration('slam_config')],
            remappings=[
                ('/scan', '/your_robot/scan')
            ]
        ),
    ])
