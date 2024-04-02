# frozen_string_literal: true

def square_of_sum (my_array, proc_square, proc_sum)
  sum = proc_sum.call(my_array)
  proc_square.call(sum)
end

proc_square_number = proc { |n| n ** 2 }
proc_sum_array = proc { |my_array| my_array.reduce(:+) }
my_array = gets.split.map(&:to_i)

puts square_of_sum(my_array, proc_square_number, proc_sum_array)
