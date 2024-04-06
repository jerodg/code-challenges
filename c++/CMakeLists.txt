cmake_minimum_required(VERSION 3.27)
project(c__)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(code_wars)
include_directories(hackerrank)
include_directories(leet_code)

add_executable(c__
        code_wars/convert_number_to_reversed_array_of_digits.cpp
        hackerrank/2d_array_ds.cpp
        hackerrank/apple_and_orange.cpp
        hackerrank/dynamic_array.cpp
        hackerrank/number_line_jumps.cpp
        leet_code/205.cpp
        leet_code/26.cpp
        leet_code/2958.cpp
        leet_code/88.cpp
        leet_code/79.cpp
        leet_code/1614.cpp
        leet_code/27.cpp
        leet_code/1544.c
        leet_code/1544.cpp
)
