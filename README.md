# Gazebo_simulation
## TODOs
### For this assignment
- [ ] (Ayaan)Build a world in Gazebo, save to file 
- [ ] (Jacob)Place a camera on the robot 
- [ ] Get Frederiks urdf file to work 
- [ ] (Ayaan)Make the robot move around (using wheels) 
- [ ] Power point for class presentation 

### For later
- [ ] Get/try LiDAR 
- [x] Create a launchfile, or similar, to launch rviz and gazebo with the model 
    - [x] rviz with robot
    - [x] Gazebo with robot
- [ ] Make it run in the docker thingy 
- [ ] Create a world with Formula student cones 
- [ ] Create path planning 

## Runing rviz and gazebo with a model using launch files
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

## Run Gazebo
Note: Ubuntu 24.04 running with wayland have an issue. As stated [here](https://gazebosim.org/docs/harmonic/troubleshooting/#wayland-issues) the workaround is to run with the prefix `QT_QPA_PLATFORM=xcb`.
```sh
gz sim empty.sdf
```

## Spawn model in Gazebo
To spawn the model inside Gazebo, run the following
```sh
gz service -s /world/empty/create --reqtype gz.msgs.EntityFactory --reptype gz.msgs.Boolean --timeout 1000 --req 'sdf_filename: "src/my_robot/urdf/hello.urdf", name: "urdf_model"'
```
