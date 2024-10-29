import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import LogInfo

def generate_launch_description():
    # Define LaunchConfigurations with default values
    pkg_name = 'my_robot'
    path_config = LaunchConfiguration('path', default='config/urdf.rviz')

    # Set up the rviz_config_path with a dynamic substitution for runtime resolution
    rviz_config_path = [get_package_share_directory(pkg_name), '/', path_config]

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_path]
    )

    return LaunchDescription([
        rviz_node
    ])
