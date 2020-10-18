cmake_minimum_required(VERSION 3.10.2)
project(diff_eq C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_REQUIRED_LIBRARIES m)

add_executable(diff_eq main.c methods.h methods.c)

target_link_libraries(diff_eq m)
