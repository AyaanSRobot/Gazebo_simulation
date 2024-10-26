import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch import LaunchContext
import xacro

""" 
    Run the robot_state_publisher package with an xacro file

    Finds the xacro file and "compiles" it to one file, then it gets published
    with robot_state_publisher.

    GitHub of robot_state_publisher: https://github.com/ros/robot_state_publisher
"""

def generate_launch_description():
    # LaunchContext is used to get input parameters and convert to string
    context = LaunchContext()

    # Get the param from launch parameters
    context.launch_configurations['pkg_name'  ] = 'my_robot'
    context.launch_configurations['model_dir' ] = 'urdf'
    context.launch_configurations['model_name'] = 'hello.urdf.xacro'
    pkg_name_config = LaunchConfiguration('pkg_name')
    model_dir_config = LaunchConfiguration('model_dir')
    model_name_config = LaunchConfiguration('model_name')

    # Get the string value of pkg_name
    pkg_name   = pkg_name_config  .perform(context)
    model_dir  = model_dir_config .perform(context)
    model_name = model_name_config.perform(context)
    
    # Get the full/global path
    xacro_file_fullpath = os.path.join(
        get_package_share_directory(pkg_name),
        model_dir,
        model_name
        )

    # Use xacro to process the file
    xacro_file_string = xacro.process_file(xacro_file_fullpath).toxml() 
    
    # Configure the node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': xacro_file_string}] # add other parameters here if required
    )

    # Run the node
    return LaunchDescription([
        node_robot_state_publisher
    ])
