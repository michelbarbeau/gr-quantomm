# Install script for directory: /home/barbeau/gr-quantomm/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/quantomm" TYPE FILE FILES
    "/home/barbeau/gr-quantomm/python/__init__.py"
    "/home/barbeau/gr-quantomm/python/encoder.py"
    "/home/barbeau/gr-quantomm/python/channel_ii.py"
    "/home/barbeau/gr-quantomm/python/decoder.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/quantomm" TYPE FILE FILES
    "/home/barbeau/gr-quantomm/build/python/__init__.pyc"
    "/home/barbeau/gr-quantomm/build/python/encoder.pyc"
    "/home/barbeau/gr-quantomm/build/python/channel_ii.pyc"
    "/home/barbeau/gr-quantomm/build/python/decoder.pyc"
    "/home/barbeau/gr-quantomm/build/python/__init__.pyo"
    "/home/barbeau/gr-quantomm/build/python/encoder.pyo"
    "/home/barbeau/gr-quantomm/build/python/channel_ii.pyo"
    "/home/barbeau/gr-quantomm/build/python/decoder.pyo"
    )
endif()

