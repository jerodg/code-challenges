cmake_minimum_required(VERSION 3.28)
project(cpp)

set(CMAKE_CXX_STANDARD 26)

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
        leet_code/1544.cpp
        hackerrank/problem_solving_basic_skills_certification/parallel_processing.cpp
        leet_code/678.cpp
        leet_code/1700.cpp
        leet_code/2073.cpp
        leet_code/950.cpp
        leet_code/988.cpp
        leet_code/463.cpp
        leet_code/200.cpp
)
