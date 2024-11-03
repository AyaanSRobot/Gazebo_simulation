import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import SetEnvironmentVariable

"""
    Master launch file

    Chosse another world by adding the following to the arguments
    world:=path/to/world.world
"""

def generate_launch_description():

    pkg_name = 'my_robot'
    pkg_share_directory = get_package_share_directory(pkg_name)

    # -------------

    # robot_state_publisher
    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(pkg_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'false', 'use_ros2_control': 'true'}.items()
    )

    # TODO Joystik things here
    joystick = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    pkg_share_directory,'launch','joystick.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    twist_mux_params = os.path.join(pkg_share_directory, 'config', 'twist_mux.yaml')
    twist_mux = Node(
        package="twist_mux",
        executable="twist_mux",
        parameters=[twist_mux_params, {'use_sim_time': True}],
        remappings=[('/cmd_vel_out','/diff_cont/cmd_vel_unstamped')]
    )

    # joint_state_publisher. Note: Also an GUI version - add (_gui)
        # GitHub: https://github.com/ros/joint_state_publisher
    jsp = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
    )

    default_rviz_config = os.path.join('config', 'normal.rviz')
    rviz_arg = DeclareLaunchArgument(
        'rviz_config',
        default_value=default_rviz_config,
        description='Rviz config to load'
    )
    rviz_config = LaunchConfiguration('rviz_config')

    rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            pkg_share_directory, 'launch', 'rviz.launch.py'
        )]),
        launch_arguments={
            'path' : rviz_config
        }.items()
    )

    # World
    default_world = os.path.join(
        pkg_share_directory,
        'worlds',
        'empty.world'
        ) 

    world_arg = DeclareLaunchArgument(
        'world',
        default_value=default_world,
        description='World to load'
    )
    world = LaunchConfiguration('world')

    # Include the Gazebo launch file, provided by the ros_gz_sim package

    # Set the environment variable
    set_qt_platform = SetEnvironmentVariable('QT_QPA_PLATFORM', 'xcb')

    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
                    launch_arguments={
                        'gz_args': ['-r -v4 ', world], 
                        'on_exit_shutdown': 'true'
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
    
    bridge_params = os.path.join(get_package_share_directory(pkg_name),
                                 'config',
                                 'gz_bridge.yaml')
    
    ros_gz_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            '--ros-args',
            '-p',
            f'config_file:={bridge_params}'
        ]
    )

    ros_gz_image_bridge = Node(
        package="ros_gz_image",
        executable="image_bridge",
        arguments=["/camera/image_raw"]
    )

    return LaunchDescription([
        rviz_arg,
        world_arg,
        rsp,
        #
        # joystick,
        twist_mux,
        #
        # jsp,
        # rviz,
        set_qt_platform,    # Used when running wayland
        gazebo,
        spawn_entity,
        ros_gz_bridge,
        ros_gz_image_bridge,
    ])