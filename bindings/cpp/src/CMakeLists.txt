
include_directories(${CMAKEDEMO_SOURCE_DIR}/src)
link_directories(${CMAKEDEMO_BINARY_DIR}/src)

#these are all compiled the same way
set(PROGRAMS test)
set ( CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH} ~/cpp-netlib-build )
find_package ( cppnetlib 0.11.0 REQUIRED )
include_directories ( ${CPPNETLIB_INCLUDE_DIRS} )

find_package(Boost COMPONENTS system filesystem thread REQUIRED)
include_directories ( ${Boost_INCLUDE_DIRS} )
include_directories(/usr/local/include)

set(JANSSON_LIB /usr/local/lib/libjansson.a)

set(ZMQ_LIB /usr/local/lib/libzmq.a)

set(
    CORELIBS
    ${CPPNETLIB_LIBRARIES}
    ${Boost_LIBRARIES}
    ${Boost_FILESYSTEM_LIBRARY}
    ${Boost_SYSTEM_LIBRARY}
    ${Boost_THREAD_LIBRARY}
    ${ZMQ_LIB}
    ${JANSSON_LIB}
)

foreach(program ${PROGRAMS})
  add_executable(${program} ${program}.cpp)
  target_link_libraries(${program} ${CORELIBS})
endforeach(program)

#building just a library. 
add_library(testlib test.cpp)

# add_executable(test_geometry test_geometry.cpp)
#linking against a custom library
# target_link_libraries(test_geometry ${CORELIBS} geometry)
