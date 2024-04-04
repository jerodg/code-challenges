# frozen_string_literal: true

# @param {String} s
# @return {Integer}
def max_depth(s)
  max = 0
  count = 0
  s.each_char do |c|
    if c == '('
      count += 1
      max = count if count > max
    elsif c == ')'
      count -= 1
    end
  end
  max
end