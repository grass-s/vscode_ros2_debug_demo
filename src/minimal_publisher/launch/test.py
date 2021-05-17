# Requirements:
#   A realsense D400 series
#   Install realsense2 ros2 package (refactor branch)
# Example:
#   $ ros2 run realsense_node realsense_node
#   $ ros2 launch rtabmap_ros realsense_d400.launch.py

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    remappings=[
          ('topic', '/hahaha/hihihi')]

    return LaunchDescription([
        # Set env var to print messages to stdout immediately
        SetEnvironmentVariable('RCUTILS_CONSOLE_STDOUT_LINE_BUFFERED', '1'),

        # Nodes to launch
        Node(
            package='examples_rclcpp_minimal_publisher',
            executable='publisher_not_composable', 
            remappings=remappings,
            #prefix=['gdb -ex run --args'],
            output='screen'),
    ])
