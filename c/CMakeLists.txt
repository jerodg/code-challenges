cmake_minimum_required(VERSION 3.28)
project(c C)

set(CMAKE_C_STANDARD 23)

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
        hackerrank/arrays_and_strings_dynamic_array.c
        hackerrank/conditionals_and_loops_conditional_statements.c
        hackerrank/conditionals_and_loops_for_loop.c
        hackerrank/conditionals_and_loops_sum_of_digits_of_a_five_digit_number.c
        hackerrank/conditionals_and_loops_bitwise_operators.c
        hackerrank/conditionals_and_loops_printing_pattern_using_loops.c
        hackerrank/structs_and_enums_small_triangles_large_triangles.c
        hackerrank/structs_and_enums_post_transition.c
        leet_code/1249.c
        leet_code/678.c
        leet_code/1700.c
        leet_code/2073.c
        leet_code/950.c
        leet_code/988.c
        leet_code/463.c
        leet_code/200.c
        leet_code/1971.c
        leet_code/1992.c
        leet_code/623.c
        leet_code/2370.c
        leet_code/2441.c
        leet_code/1915.c
        leet_code/1289.c
        leet_code/165.c)
