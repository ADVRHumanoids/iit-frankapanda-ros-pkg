cmake_minimum_required(VERSION 3.0)

set(ROBOT_NAME inail2arm)
project(iit-${ROBOT_NAME}-ros-pkg VERSION 1.0.0)

include(GenerateXrdf.cmake)

## add sub-packages
add_subdirectory(inail2arm_urdf)
add_subdirectory(inail2arm_srdf)
add_subdirectory(inail2arm_gazebo)
add_subdirectory(inail2arm_config)
add_subdirectory(inail2arm_cartesio)

