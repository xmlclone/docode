cmake_minimum_required(VERSION 3.7)
project(testCcode C)

set(CMAKE_C_STANDARD 99)

add_library(my_c_code SHARED my_c_code.c)
add_library(encry SHARED encry.c)