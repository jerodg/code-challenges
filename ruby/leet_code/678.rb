# frozen_string_literal: true

# @param {String} s
# @return {Boolean}
# @param [Object] s
def check_valid_string(s)
  low = 0
  high = 0
  (0...s.length).each do |i|
    if s[i] == '('
      low += 1
      high += 1
    elsif s[i] == ')'
      low -= 1
      high -= 1
    else
      low -= 1
      high += 1
    end
    low = [low, 0].max
    return false if low > high
  end
  low.zero?
end