cmake_minimum_required(VERSION 3.0)
project(frankapanda_config)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY hal
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(FILES frankapanda.yaml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
