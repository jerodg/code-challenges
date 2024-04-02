# frozen_string_literal: true

def prime?(x)
  return false if x < 2

  checker = Math.sqrt(x).to_i # 4
  2.upto(checker).each { |i| return false if x % i == 0 }

  true
end

palindrome_array = -> (array_size) do
  2.upto(Float::INFINITY).lazy.select do |x|
    prime?(x) && x.digits.join.to_i == x
  end.first(array_size.to_i)
end

N = gets
print palindrome_array.(N.to_i)