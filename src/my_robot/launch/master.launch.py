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

    pkg_name = 'my_robot'
    pkg_share_directory = get_package_share_directory(pkg_name)

    # -------------

    # robot_state_publisher
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            # Directory to: install/pkg_name/share/pkg_name
            pkg_share_directory,
            'launch',       # name of folder
            'rsp.launch.py' # name of file
        )]), 
        launch_arguments={'pkg_name': pkg_name,
                          'model_dir': 'urdf',
                          'model_name': 'hello.urdf.xacro' 
                          }.items()
    )

    # joint_state_publisher. Note: Also an GUI version
        # GitHub: https://github.com/ros/joint_state_publisher
    jsp = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
    )

    rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            pkg_share_directory, 'launch', 'rviz.launch.py'
        )]),
    )

    return LaunchDescription([
        rsp,
        jsp,
        rviz
    ])