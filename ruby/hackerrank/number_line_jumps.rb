#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2)
  if v1 > v2
    if (x2 - x1) % (v1 - v2) == 0
      return "YES"
    end
  end
  "NO"
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

first_multiple_input = gets.rstrip.split

x1 = first_multiple_input[0].to_i

v1 = first_multiple_input[1].to_i

x2 = first_multiple_input[2].to_i

v2 = first_multiple_input[3].to_i

result = kangaroo x1, v1, x2, v2

fptr.write result
fptr.write "\n"

fptr.close()
