# Gazebo_simulation
## TODOs
### For this assignment
- [ ] Build a world in Gazebo, save to file
- [ ] Place a camera on the robot
- [ ] Get Frederiks urdf file to work
- [ ] Make the robot move around (using wheels)
- [ ] Power point for class presentation

### For later
- [ ] Get/try LiDAR  
- [ ] Create a launchfile, or similar, to laucnh rviz and gazebo with the model
- [ ] Make it run in the docker thingy
- [ ] Create a world with Formula student cones
- [ ] Create path planning

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

## Run Gazebo
On Jacobs computer, he needs to run with the prefix `QT_QPA_PLATFORM=xcb`, else the program will crash
```sh
QT_QPA_PLATFORM=xcb gz sim empty.sdf
```

## Spawn model in Gazebo
To spawn the model inside Gazebo, run the following
Note: You need to change the path
```sh
gz service -s /world/empty/create --reqtype gz.msgs.EntityFactory --reptype gz.msgs.Boolean --timeout 1000 --req 'sdf_filename: "/home/jrz/workspace/Gazebo_simulation/src/my_robot/urdf/hello.urdf", name: "urdf_model"'
```
