cmake_minimum_required(VERSION 3.27)
project(c C)

set(CMAKE_C_STANDARD 11)

include_directories(.)
include_directories(code_wars)
include_directories(hackerrank)
include_directories(leet_code)

add_executable(c
        leet_code/205.c
        leet_code/26.c
        leet_code/88.c
        leet_code/2958.c
        leet_code/79.c)
