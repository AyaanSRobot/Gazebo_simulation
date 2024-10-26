import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node

def generate_launch_description():

    package_name = 'my_robot'
    # TODO: Get package path and use it as parameter for rsp and rviz

    # robot_state_publisher
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','rsp.launch.py'
        )]), 
        # launch_arguments={'use_sim_time': 'true', 'use_ros2_control': 'true'}.items()
    )

    # joint_state_publisher. Note: Also an GUI version
        # GitHub: https://github.com/ros/joint_state_publisher
    jsp = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
    )

    rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','rviz.launch.py'
        )]),
    )

    return LaunchDescription([
        rsp,
        jsp,
        rviz
    ])