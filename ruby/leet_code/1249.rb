# frozen_string_literal: true

# @param {String} s
# @return {String}
# @param [Object] s
def min_remove_to_make_valid(s)
  stack = []
  removed_indices = Set.new

  s.each_char.with_index do |char, idx|
    if char == '('
      stack << idx
    elsif char == ')'
      if stack.empty?
        removed_indices << idx
      else
        stack.pop
      end
    end
  end

  stack.each do |idx|
    removed_indices << idx
  end

  s.chars.each_with_index.map { |char, idx| removed_indices.include?(idx) ? nil : char }.compact.join
end
