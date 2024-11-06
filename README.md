# Gazebo simulation
## TODOs
### For this assignment
- [x] Place a camera on the robot 
    - [x] Make the camera visaul in rviz world
- [x] Make the robot move around (using wheels and keyboard)
- [x] Power point for class presentation 
- [ ] Build a world in Gazebo, save to file
- [ ] Implement Ackermann steering (use the branch)
- [ ] Get Frederiks urdf file to work 
- [ ] Documentation

### For later
- [ ] Get/try LiDAR 
- [x] Create a launchfile, or similar, to launch rviz and gazebo with the model 
    - [x] rviz with robot
    - [x] Gazebo with robot
- [ ] Make it run in the docker thingy / move to ROS repo
- [ ] Create a world with Formula student cones 
- [ ] Create path planning


## Using the launchfile
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

Then run rviz and gazebo with a robot
```sh
ros2 launch my_robot master.launch.py
```

### Launch file parameters
#### Gazebo World
You can specify which `world` to run by providing its path; for example, launch `cylinder.world` with:
```sh
ros2 launch my_robot master.launch.py world:=./src/my_robot/worlds/cylinder.world
```
The default is `empty.world`.

#### Rviz config
You can specify which `rviz_config` to use by providing its path; for example, launch `urdf.rviz` with:
```sh
ros2 launch my_robot master.launch.py rviz_config:=config/urdf.rviz
```

### Running Gazebo on Ubuntu 24.04 with Wayland
Note: Ubuntu 24.04 running with wayland have an issue. As stated [here](https://gazebosim.org/docs/harmonic/troubleshooting/#wayland-issues) the workaround is to run with the prefix `QT_QPA_PLATFORM=xcb`.
```sh
QT_QPA_PLATFORM=xcb gz sim empty.sdf
```

### Run teletop thing
```sh
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
