cmake_minimum_required(VERSION 3.5)
project(human_detection)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)

install(
    PROGRAMS
        src/human_detection_node.py
    DESTINATION lib/${PROJECT_NAME}
)

ament_package()
