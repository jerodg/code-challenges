# @param {String} s
# @return {String}
def make_good(s)
  stack = []
  s.each_char do |c|
    if stack.empty?
      stack.push(c)
    else
      if stack.last.downcase == c.downcase && stack.last != c
        stack.pop
      else
        stack.push(c)
      end
    end
  end
  stack.join
end