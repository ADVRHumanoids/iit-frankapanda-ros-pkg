# Franka Description

*This is the models to use to use the franka panda with only ROS (1, noetic), and NO XBOT*
*So please use this and not the binary installed with ros-noetic-franka-description*

Code taken from https://github.com/frankaemika/franka_ros.git (from the main branch, ie `develop`) since:

- `noetic` binary has the parent always as world (from the `noetic` branch I suppose)
- Separate repo https://github.com/frankaemika/franka_description seems related to ROS2

Also slightly modified for some things like having a mounting base, to solve some problems like possibility to use a platform only when using gazebo.

