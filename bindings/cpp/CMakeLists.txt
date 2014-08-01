
cmake_minimum_required(VERSION 2.8.3)
project(ZMQROSCPP)

#There are lots of scripts with cmake
#for finding external libraries. 
#see /usr/local/share/cmake-2.6/Modules/Find*.cmake for more examples

set(CMAKE_CXX_FLAGS "-g -Wall")
add_subdirectory(src)
