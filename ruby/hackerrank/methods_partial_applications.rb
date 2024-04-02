# frozen_string_literal: true

combination = -> (n) do -> (r) do
    (1..n).reduce(:*) / ((1..r).reduce(:*) * (1..(n - r)).reduce(:*))
  end
end

  n = gets.to_i
r = gets.to_i
ncr = combination.(n)
puts ncr.(r)