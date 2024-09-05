from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    return LaunchDescription([
        # Include Gazebo world launch file
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                '/home/tishan-kashmeera/Desktop/disaster_response-drone_simulation/launch/gazebo_world.launch.py'
            ]),
            launch_arguments={}.items()
        ),

        # Include SLAM launch file
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                '/home/tishan-kashmeera/Desktop/disaster_response-drone_simulation/launch/slam_launch.py'
            ]),
            launch_arguments={}.items()
        ),

        # Include Human Detection launch file
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                '/home/tishan-kashmeera/Desktop/disaster_response-drone_simulation/launch/human_detection_launch.py'
            ]),
            launch_arguments={}.items()
        ),
    ])
