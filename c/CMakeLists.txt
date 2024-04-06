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
        leet_code/79.c
        leet_code/27.c
        leet_code/1614.c
        code_wars/convert_number_to_reversed_array_of_digits.c
        hackerrank/introduction_hello_world.c
        hackerrank/introduction_playing_with_characters.c
        hackerrank/introduction_sum_and_difference_of_two_numbers.c
        hackerrank/introduction_functions.c
        hackerrank/introduction_pointers.c
        hackerrank/functions_sorting_array_of_strings.c
        hackerrank/functions_permutations_of_strings.c
        hackerrank/functions_variadic.c
        hackerrank/functions_querying_the_document.c
        leet_code/1544.c
        hackerrank/functions_calculate_the_nth_term.c
        hackerrank/functions_students_marks_sums.c
        hackerrank/arrays_and_strings_digit_frequency.c
        hackerrank/arrays_and_strings_dynamic_array.c)
