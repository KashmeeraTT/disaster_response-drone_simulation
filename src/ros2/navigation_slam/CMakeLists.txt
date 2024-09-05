cmake_minimum_required(VERSION 3.5)
project(navigation_slam)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(nav_msgs REQUIRED)

install(
    PROGRAMS
        src/slam_node.py
    DESTINATION lib/${PROJECT_NAME}
)

ament_package()
