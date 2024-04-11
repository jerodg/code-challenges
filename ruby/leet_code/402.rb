# @param {String} num
# @param {Integer} k
# @return {String}
def remove_kdigits(num, k)
  # If the length of the number is equal to k, return "0"
  return '0' if num.length == k

  # Create a stack and iterate over each character in the number
  stack = num.each_char.with_object([]) do |digit, stack|
    # While the stack is not empty, k is not zero, and the current digit is less than the last digit in the stack
    # decrement k and pop the last digit from the stack
    k, = k.pred, stack.pop until stack.empty? || k.zero? || digit.to_i >= stack.last.to_i

    # Push the current digit onto the stack
    stack << digit
  end

  # Pop k digits from the stack
  k.times { stack.pop }

  # Remove leading zeros from the stack
  stack.shift until stack.first != '0'

  # If the stack is empty, return "0", otherwise join the stack into a string and return it
  stack.empty? ? '0' : stack.join
end