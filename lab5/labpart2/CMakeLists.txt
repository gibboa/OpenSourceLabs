cmake_minimum_required(VERSION 3.0)
project(lab5_cmake_static)

add_library(prog_lib STATIC source/block.c headers/block.h)

add_executable(cmaked_prog_static program.c)
target_link_libraries(cmaked_prog_static prog_lib)
