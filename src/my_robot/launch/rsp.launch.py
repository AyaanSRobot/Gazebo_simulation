import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro

""" 
    Run the robot_state_publisher package with an xacro file

    Finds the xacro file and "compiles" it to one file, then it gets published
    with robot_state_publisher.

    GitHub of robot_state_publisher: https://github.com/ros/robot_state_publisher
"""

def generate_launch_description():

    # TODO: Get pkg and filename as input
    # Specify the name of the package and path to xacro file within the package
    pkg_name = 'my_robot'
    file_name = 'urdf/hello.urdf.xacro'
    
    # Get the full/global path
    xacro_file_fullpath = os.path.join(get_package_share_directory(pkg_name),
                       file_name)

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
