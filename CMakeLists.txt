cmake_minimum_required(VERSION 3.0)

set(ROBOT_NAME frankapanda)
project(iit-${ROBOT_NAME}-ros-pkg VERSION 1.0.0)

include(GenerateXrdf.cmake)

## add sub-packages
add_subdirectory(frankapanda_urdf)
add_subdirectory(frankapanda_srdf)
add_subdirectory(frankapanda_gazebo)
add_subdirectory(frankapanda_config)
add_subdirectory(frankapanda_cartesio)

