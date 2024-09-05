from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '/home/tishan-kashmeera/Desktop/disaster_response-drone_simulation/worlds/disaster_world.world'],
            output='screen'),
    ])
