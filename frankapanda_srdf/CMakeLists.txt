project(${ROBOT_NAME}_srdf)

find_package(catkin REQUIRED)

catkin_package()

# main srdf, with acm
generate_srdf(
  XACRO ${ROBOT_NAME}.srdf.xacro 
  CONFIG config/${ROBOT_NAME}.urdf.xacro 
  ADD_TO_ALL TRUE
  GEN_ACM TRUE
)

# mark srdf for installation
install(DIRECTORY srdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
