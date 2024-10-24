# Gazebo_simulation

## Runing the rviz simulation
Make sure to have sourced the ROS installation as the 'underlay'.

Be sure to be in the ROS soruce folder `Gazebo_simulation`. 

Then build the workspace with
```sh
colcon build
```

Source the 'overlay' with
```sh
source install/local_setup.sh
```

Then run rviz with a model with
```sh
ros2 launch my_robot display.launch.py model:=hello.urdf
```