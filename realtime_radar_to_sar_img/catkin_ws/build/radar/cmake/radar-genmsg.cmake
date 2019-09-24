# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "radar: 3 messages, 0 services")

set(MSG_I_FLAGS "-Iradar:/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(radar_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/raw.msg" NAME_WE)
add_custom_target(_radar_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "radar" "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/raw.msg" ""
)

get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/rail.msg" NAME_WE)
add_custom_target(_radar_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "radar" "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/rail.msg" ""
)

get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/wav.msg" NAME_WE)
add_custom_target(_radar_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "radar" "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/wav.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/raw.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/radar
)
_generate_msg_cpp(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/rail.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/radar
)
_generate_msg_cpp(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/wav.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/radar
)

### Generating Services

### Generating Module File
_generate_module_cpp(radar
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/radar
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(radar_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(radar_generate_messages radar_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/raw.msg" NAME_WE)
add_dependencies(radar_generate_messages_cpp _radar_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/rail.msg" NAME_WE)
add_dependencies(radar_generate_messages_cpp _radar_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/wav.msg" NAME_WE)
add_dependencies(radar_generate_messages_cpp _radar_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(radar_gencpp)
add_dependencies(radar_gencpp radar_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS radar_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/raw.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/radar
)
_generate_msg_eus(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/rail.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/radar
)
_generate_msg_eus(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/wav.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/radar
)

### Generating Services

### Generating Module File
_generate_module_eus(radar
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/radar
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(radar_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(radar_generate_messages radar_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/raw.msg" NAME_WE)
add_dependencies(radar_generate_messages_eus _radar_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/rail.msg" NAME_WE)
add_dependencies(radar_generate_messages_eus _radar_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/wav.msg" NAME_WE)
add_dependencies(radar_generate_messages_eus _radar_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(radar_geneus)
add_dependencies(radar_geneus radar_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS radar_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/raw.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/radar
)
_generate_msg_lisp(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/rail.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/radar
)
_generate_msg_lisp(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/wav.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/radar
)

### Generating Services

### Generating Module File
_generate_module_lisp(radar
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/radar
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(radar_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(radar_generate_messages radar_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/raw.msg" NAME_WE)
add_dependencies(radar_generate_messages_lisp _radar_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/rail.msg" NAME_WE)
add_dependencies(radar_generate_messages_lisp _radar_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/wav.msg" NAME_WE)
add_dependencies(radar_generate_messages_lisp _radar_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(radar_genlisp)
add_dependencies(radar_genlisp radar_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS radar_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/raw.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/radar
)
_generate_msg_nodejs(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/rail.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/radar
)
_generate_msg_nodejs(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/wav.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/radar
)

### Generating Services

### Generating Module File
_generate_module_nodejs(radar
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/radar
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(radar_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(radar_generate_messages radar_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/raw.msg" NAME_WE)
add_dependencies(radar_generate_messages_nodejs _radar_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/rail.msg" NAME_WE)
add_dependencies(radar_generate_messages_nodejs _radar_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/wav.msg" NAME_WE)
add_dependencies(radar_generate_messages_nodejs _radar_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(radar_gennodejs)
add_dependencies(radar_gennodejs radar_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS radar_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/raw.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/radar
)
_generate_msg_py(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/rail.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/radar
)
_generate_msg_py(radar
  "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/wav.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/radar
)

### Generating Services

### Generating Module File
_generate_module_py(radar
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/radar
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(radar_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(radar_generate_messages radar_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/raw.msg" NAME_WE)
add_dependencies(radar_generate_messages_py _radar_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/rail.msg" NAME_WE)
add_dependencies(radar_generate_messages_py _radar_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/project/cuav/realtime_radar_to_sar_img/catkin_ws/src/radar/msg/wav.msg" NAME_WE)
add_dependencies(radar_generate_messages_py _radar_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(radar_genpy)
add_dependencies(radar_genpy radar_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS radar_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/radar)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/radar
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(radar_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/radar)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/radar
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(radar_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/radar)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/radar
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(radar_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/radar)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/radar
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(radar_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/radar)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/radar\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/radar
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(radar_generate_messages_py std_msgs_generate_messages_py)
endif()
