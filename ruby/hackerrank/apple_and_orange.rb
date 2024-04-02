#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges)
  apple_count = 0
  orange_count = 0

  apples.each do |apple|
    apple_count += 1 if (a + apple).between?(s, t)
  end

  oranges.each do |orange|
    orange_count += 1 if (b + orange).between?(s, t)
  end

  puts apple_count
  puts orange_count
end

first_multiple_input = gets.rstrip.split

s = first_multiple_input[0].to_i

t = first_multiple_input[1].to_i

second_multiple_input = gets.rstrip.split

a = second_multiple_input[0].to_i

b = second_multiple_input[1].to_i

third_multiple_input = gets.rstrip.split

m = third_multiple_input[0].to_i

n = third_multiple_input[1].to_i

apples = gets.rstrip.split.map(&:to_i)

oranges = gets.rstrip.split.map(&:to_i)

countApplesAndOranges s, t, a, b, apples, oranges
