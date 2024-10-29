import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch import LaunchContext

from launch_ros.actions import Node

def generate_launch_description():
    # TODO: Get pkg and filename as input
    context = LaunchContext()

    # Default values
    context.launch_configurations['pkg_name'] = 'my_robot'
    context.launch_configurations['path'] = 'config/urdf.rviz'

    #
    pkg_name_config = LaunchConfiguration('pkg_name')
    path_config = LaunchConfiguration('path')

    # Exstract thestring
    pkg_name   = pkg_name_config.perform(context)
    file_name   = path_config.perform(context)

    # pkg_name = 'my_robot'
    # file_name = 'config/urdf.rviz'

    # Get the full/global path
    rviz_config_path = os.path.join(
        get_package_share_directory(pkg_name),
        file_name
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output = 'screen',
        arguments=['-d', rviz_config_path]
    )

    return LaunchDescription([
        rviz_node
    ])