cmake_minimum_required(VERSION 3.20)
project(micro-example)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

add_library(micro-example SHARED algorithm.cc c_wrapper.cc)
