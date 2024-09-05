from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # SLAM Node
        Node(
            package='navigation_slam',
            executable='slam_node',
            name='slam_node',
            output='screen',
            parameters=['/home/tishan-kashmeera/Desktop/disaster_response-drone_simulation/configs/slam_configs.yaml']),

        # AMCL (Adaptive Monte Carlo Localization) for localization
        Node(
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=['/home/tishan-kashmeera/Desktop/disaster_response-drone_simulation/configs/nav2_params.yaml']),

        # Map Server to load the map and handle navigation
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=['/home/tishan-kashmeera/Desktop/disaster_response-drone_simulation/configs/nav2_params.yaml']),

        # Planner for path planning
        Node(
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=['/home/tishan-kashmeera/Desktop/disaster_response-drone_simulation/configs/nav2_params.yaml']),

        # Controller for following paths
        Node(
            package='nav2_controller',
            executable='controller_server',
            name='controller_server',
            output='screen',
            parameters=['/home/tishan-kashmeera/Desktop/disaster_response-drone_simulation/configs/nav2_params.yaml']),

        # Lifecycle Manager to manage the lifecycle of Nav2 nodes
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_navigation',
            output='screen',
            parameters=[{'use_sim_time': True},
                        {'autostart': True},
                        {'node_names': ['map_server', 'planner_server', 'controller_server', 'amcl']}])
    ])
