import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import SetEnvironmentVariable

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

    # Include the Gazebo launch file, provided by the ros_gz_sim package

    # Set the environment variable
    set_qt_platform = SetEnvironmentVariable('QT_QPA_PLATFORM', 'xcb')

    default_world = os.path.join(
        pkg_share_directory,
        'worlds',
        'empty.world'
        )  
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
                    launch_arguments={
                        'gz_args': f'-r -v4 {default_world}',
                        'on_exit_shutdown': 'false'
                    }.items()
             )


    # Taken from: https://github.com/joshnewans/articubot_one/blob/new_gazebo/launch/launch_sim.launch.py
    # Run the spawner node from the ros_gz_sim package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='ros_gz_sim', 
                        executable='create',
                        arguments=['-topic', 'robot_description',
                                   '-name', 'my_bot',
                                   '-z', '0.1'],
                        output='screen')

    return LaunchDescription([
        rsp,
        jsp,
        rviz,
        set_qt_platform,    # Used when running wayland
        gazebo,
        spawn_entity,
    ])