# Gazebo_simulation
## TODOs
### For this assignment
- [ ] (Jacob)Build a world in Gazebo, save to file 
- [x] (Jacob)Place a camera on the robot 
    - [x] Make the camera visaul in rviz world
- [ ] Get Frederiks urdf file to work 
- [ ] (Ayaan)Make the robot move around (using wheels and keyboard)
- [ ] Power point for class presentation 

### For later
- [ ] Get/try LiDAR 
- [x] Create a launchfile, or similar, to launch rviz and gazebo with the model 
    - [x] rviz with robot
    - [x] Gazebo with robot
- [ ] Make it run in the docker thingy 
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

### Parameters
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

#### Robot
```sh

```

### What does the master.launch.py do?
TODO: Descripe which commands I run, and how to run them without the launch file. And what they do / why are they needed
TODO: Explain Gazebo topics and how to connect to ROS

#### Rviz config
```sh
ros2 launch my_robot rviz.launch.py
```
or just `rviz2`

### Run Gazebo
Note: Ubuntu 24.04 running with wayland have an issue. As stated [here](https://gazebosim.org/docs/harmonic/troubleshooting/#wayland-issues) the workaround is to run with the prefix `QT_QPA_PLATFORM=xcb`.
```sh
gz sim empty.sdf
```

### Spawn model in Gazebo
To spawn the model inside Gazebo, run the following
```sh
gz service -s /world/empty/create --reqtype gz.msgs.EntityFactory --reptype gz.msgs.Boolean --timeout 1000 --req 'sdf_filename: "src/my_robot/urdf/hello.urdf", name: "urdf_model"'
```
